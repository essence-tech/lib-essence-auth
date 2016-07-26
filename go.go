package client

import (
	"crypto/md5"
	_ "crypto/sha512" // Fixes SSL
	"crypto/tls"
	"crypto/x509"
	"encoding/hex"
	"encoding/json"
	"errors"
	"golang.org/x/net/publicsuffix"
	"io/ioutil"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"sort"
	"strings"
	"time"
)

var (
	// ErrCertificatesFail error on get a certificate pool.
	ErrCertificatesFail = errors.New("Failed to get certificate pool")
)

// AuthError An error from or about the auth service
type AuthError struct {
	Code int
	msg  string
}

func (e AuthError) Error() string {
	return e.msg
}

// App describes an application in the Auth service.
type App struct {
	Host string
	ID   string
	Key  string
	user *User

	InsecureSkip        *bool
	CertificateLocation *string

	transport *http.Transport
}

// User describes a user in the Auth service.
type User struct {
	Email           string       `json:"email"`
	Name            string       `json:"name"`
	Picture         string       `json:"picture"`
	Apps            []AuthApp    `json:"apps"`
	Permissions     []Permission `json:"permissions"`
	permissionSetID *string
}

// AuthApp the authentication app.
type AuthApp struct {
	ID          string       `json:"id"`
	Permissions []Permission `json:"permissions"`
}

// Permission a permission of an app.
type Permission struct {
	ID     string              `json:"id"`
	Name   string              `json:"name"`
	Values []map[string]string `json:"values"`
}

// GetUser Return the user for this request
func (a *App) GetUser(r *http.Request, siblingKeys ...string) (*User, error) {
	c, err := r.Cookie("essence_auth")
	if err != nil {
		return nil, AuthError{http.StatusUnauthorized, "Cookie not found"}
	}

	client, err := a.getClient(c, a.Host)
	if err != nil {
		return nil, AuthError{http.StatusInternalServerError, "Cannot generate auth client"}
	}

	q := url.Values{}
	q.Set("key", a.Key)
	for _, sibling := range siblingKeys {
		q.Add("key", sibling)
	}
	resp, err := client.Get(a.Host + "/me2?" + q.Encode())
	if err != nil {
		return nil, AuthError{http.StatusInternalServerError, "Cannot make successful auth request"}
	}
	resp.Close = true
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, AuthError{resp.StatusCode, "User request unsuccessful"}
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, AuthError{http.StatusInternalServerError, "Response body read unsuccessful"}
	}

	var user User
	if err := json.Unmarshal(body, &user); err != nil {
		return nil, AuthError{http.StatusInternalServerError, "User deocde unsuccessful"}
	}

	for _, app := range user.Apps {
		if app.ID == a.ID {
			user.Permissions = app.Permissions
			break
		}
	}

	return &user, nil
}

// SetPermissions allows an app to set its own permisisons with the auth service.
func (a App) SetPermissions(permissions ...Permission) error {
	data, err := json.Marshal(permissions)
	if err != nil {
		return err
	}

	url := a.Host + "/api/v1/apps/" + a.ID + "?key=" + a.Key
	_, err = http.Post(url, "application/json", strings.NewReader(string(data)))
	return err
}

// HasPermission does a user have a specific permission
func (u User) HasPermission(id string) bool {
	for _, p := range u.Permissions {
		if p.ID == id {
			return true
		}
	}
	return false
}

// GetValue does a user have a specific value.
func (u User) GetValue(id string) (string, error) {
	for _, p := range u.Permissions {
		for _, values := range p.Values {
			if v, ok := values[id]; ok {
				return v, nil
			}
		}
	}
	return "", AuthError{0, "Value not found"}
}

// PermissionSetID gets a repeatable identifier for this users set of Permissions.
func (u *User) PermissionSetID() string {
	if u.permissionSetID != nil {
		return *u.permissionSetID
	}

	keys := []string{}
	for _, p := range u.Permissions {
		collect := []string{}
		for _, val := range p.Values {
			for k, v := range val {
				collect = append(collect, k+"|"+v)
			}
		}
		keys = append(keys, p.ID)
		keys = append(keys, strings.Join(collect, ":"))
	}
	sort.Strings(keys)

	id := strings.Join(keys, "_")
	hashBytes := md5.Sum([]byte(id))
	hash := hex.EncodeToString(hashBytes[:])
	u.permissionSetID = &hash
	return *u.permissionSetID
}

func (a App) caCerts() (*x509.CertPool, error) {
	pemcerts, err := ioutil.ReadFile(*a.CertificateLocation)
	if err != nil {
		return nil, ErrCertificatesFail
	}

	pool := x509.NewCertPool()
	if ok := pool.AppendCertsFromPEM(pemcerts); !ok {
		return nil, ErrCertificatesFail
	}
	return pool, nil
}

func (a App) getClient(c *http.Cookie, host string) (*http.Client, error) {
	options := cookiejar.Options{PublicSuffixList: publicsuffix.List}
	u, err := url.Parse(host)
	if err != nil {
		return nil, err
	}

	jar, err := cookiejar.New(&options)
	if err != nil {
		return nil, err
	}

	jar.SetCookies(u, []*http.Cookie{c})

	if a.transport == nil {
		config := tls.Config{}
		if a.InsecureSkip != nil && *a.InsecureSkip == true {
			config.InsecureSkipVerify = true
		}

		if a.CertificateLocation != nil {
			pool, err := a.caCerts()
			if err == nil {
				config.RootCAs = pool
			}
		}

		a.transport = &http.Transport{TLSClientConfig: &config}
	}

	return &http.Client{Jar: jar, Transport: a.transport, Timeout: 1 * time.Minute}, nil
}
