package auth

import (
	"crypto/md5"
	"encoding/hex"
	"log"
	"net/http"
	"sort"
	"strings"

	"github.com/essence-tech/lib-essence-auth/essenceauth"
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
			keys = append(keys, strings.Join(collect, ":"))
		}
	}
	sort.Strings(keys)

	id := strings.Join(keys, "_")
	hashBytes := md5.Sum([]byte(id))
	return hex.EncodeToString(hashBytes[:])
}

// GenAppUserRequest creates a new application user request.
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
