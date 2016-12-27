package auth

import (
	"crypto/md5"
	"encoding/hex"
	"log"
	"net/http"
	"sort"
	"strings"
	"time"

	"github.com/essence-tech/lib-essence-auth/essenceauth"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

// Service provides access to auth.
type Service interface {
	essenceauth.EssenceAuthClient
	Close()
}

type serviceClient struct {
	essenceauth.EssenceAuthClient
	conn *grpc.ClientConn
}

// New returns a new Service instance with default options.
func New(host string) Service {
	conn, err := grpc.Dial(host, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}

	_client := essenceauth.NewEssenceAuthClient(conn)
	return &serviceClient{_client, conn}
}

// Close closes the connection to the service.
func (s *serviceClient) Close() {
	s.conn.Close()
}

// PermissionSetID gets a repeatable identifier for this users set of Permissions.
func PermissionSetID(u *essenceauth.User) string {
	keys := []string{}
	for _, a := range u.Apps {
		for _, p := range a.Permissions {
			collect := []string{}
			for _, val := range p.Values {
				collect = append(collect, val.Key+"|"+val.Value)
			}
			keys = append(keys, p.ID)
			sort.Strings(collect)
			keys = append(keys, strings.Join(collect, ":"))
		}
	}
	sort.Strings(keys)

	id := strings.Join(keys, "_")
	hashBytes := md5.Sum([]byte(id))
	return hex.EncodeToString(hashBytes[:])
}

// GenAppUserRequest a helper function to create a new application user request.
func GenAppUserRequest(appID string, appKeys []string, r *http.Request) *essenceauth.AppUserRequest {
	JWT := ""
	for _, c := range r.Cookies() {
		if c.Name == "ea" {
			JWT = c.Value
			break
		}
	}

	return &essenceauth.AppUserRequest{
		ID:   appID,
		Keys: appKeys,
		JWT:  JWT,
	}
}

// UserHasPermission a helper function to test a user for a specific permission.
func UserHasPermission(user *essenceauth.User, appID, permID string) bool {
	for _, a := range user.Apps {
		if a.ID == appID {
			for _, p := range a.Permissions {
				if p.ID == permID {
					return true
				}
			}
		}
	}
	return false
}

// PermissionsReporter helps an application report permissions regularly.
func PermissionsReporter(ID, Key string, service Service, perms []*essenceauth.Permission) {
	run := func() {
		err := setPermissions(ID, Key, service, perms)
		if err != nil {
			log.Println("Error", err)
		}
	}
	go run()

	ticker := time.NewTicker(time.Hour * 24)
	go func() {
		for _ = range ticker.C {
			go run()
		}
	}()
}

func setPermissions(ID, Key string, service Service, perms []*essenceauth.Permission) error {
	req := &essenceauth.App{
		ID:          ID,
		Key:         Key,
		Permissions: perms,
	}
	_, err := service.AppUpdateApp(context.Background(), req)
	return err
}
