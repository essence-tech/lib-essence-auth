package client

import (
	"code.google.com/p/go.net/publicsuffix"
	"crypto/md5"
	_ "crypto/sha512"
	"crypto/tls"
	"crypto/x509"
	"encoding/hex"
	"encoding/json"
	"errors"
	"io/ioutil"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"sort"
	"strings"
)

var (
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

type App struct {
	Host string
	Id   string
	Key  string
	user *User

	InsecureSkip        *bool
	CertificateLocation *string
}

type User struct {
	Email           string       `json:"email"`
	Name            string       `json:"name"`
	Picture         string       `json:"picture"`
	Apps            []AuthApp    `json:"apps"`
	Permissions     []Permission `json:"permissions"`
	permissionSetId *string      `json:"-"`
}

type AuthApp struct {
	Id          string       `json:"id"`
	Permissions []Permission `json:"permissions"`
}

type Permission struct {
	Id     string              `json:"id"`
	Name   string              `json:"name"`
	Values []map[string]string `json:"values"`
}

// GetUser Return the user for this request
func (a *App) GetUser(r *http.Request, siblingKeys ...string) (*User, error) {
	if a.user != nil {
		return a.user, nil
	}

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
		if app.Id == a.Id {
			user.Permissions = app.Permissions
			break
		}
	}

	a.user = &user
	return &user, nil
}

// Set permissions with the auth service
func (this App) SetPermissions(permissions ...Permission) error {
	data, err := json.Marshal(permissions)
	if err != nil {
		return err
	}

	url := this.Host + "/api/v1/apps/" + this.Id + "?key=" + this.Key
	_, err = http.Post(url, "application/json", strings.NewReader(string(data)))
	return err
}

// Does a user have a specific permission
func (this User) HasPermission(id string) bool {
	for _, p := range this.Permissions {
		if p.Id == id {
			return true
		}
	}
	return false
}

// Get a repeatable identifier for this users set of Permissions
func (this *User) PermissionSetId() string {
	if this.permissionSetId != nil {
		return *this.permissionSetId
	}

	keys := []string{}
	for _, p := range this.Permissions {
		collect := []string{}
		for _, val := range p.Values {
			for k, v := range val {
				collect = append(collect, k+"|"+v)
			}
		}
		keys = append(keys, p.Id)
		keys = append(keys, strings.Join(collect, ":"))
	}
	sort.Strings(keys)

	id := strings.Join(keys, "_")
	hashBytes := md5.Sum([]byte(id))
	hash := hex.EncodeToString(hashBytes[:])
	this.permissionSetId = &hash
	return *this.permissionSetId
}

func (this App) caCerts() (*x509.CertPool, error) {
	pemcerts, err := ioutil.ReadFile(*this.CertificateLocation)
	if err != nil {
		return nil, ErrCertificatesFail
	}

	pool := x509.NewCertPool()
	if ok := pool.AppendCertsFromPEM(pemcerts); !ok {
		return nil, ErrCertificatesFail
	}
	return pool, nil
}

func (this App) getClient(c *http.Cookie, host string) (*http.Client, error) {
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

	config := tls.Config{}
	if this.InsecureSkip != nil && *this.InsecureSkip == true {
		config.InsecureSkipVerify = true
	}

	if this.CertificateLocation != nil {
		pool, err := this.caCerts()
		if err == nil {
			config.RootCAs = pool
		}
	}
	return &http.Client{Jar: jar, Transport: &http.Transport{TLSClientConfig: &config}}, nil
}
