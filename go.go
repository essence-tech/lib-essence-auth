package client

import (
	"code.google.com/p/go.net/publicsuffix"
	"encoding/json"
	"errors"
	"io/ioutil"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"strings"
)

var (
	ErrUnauthorised = errors.New("Failed to get user")
)

type App struct {
	Host string
	Id   string
	Key  string
	user *User
}

type User struct {
	Email       string       `json:"email"`
	Name        string       `json:"name"`
	Picture     string       `json:"picture"`
	Apps        []AuthApp    `json:"apps"`
	Permissions []Permission `json:"permissions"`
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

// Return the user for this request
func (this *App) GetUser(r *http.Request, siblingKeys ...string) (*User, error) {
	if this.user != nil {
		return this.user, nil
	}

	c, err := r.Cookie("essence_auth")
	if err != nil {
		return nil, err
	}

	client, err := getClient(c, this.Host)
	if err != nil {
		return nil, err
	}

	q := url.Values{}
	q.Set("key", this.Key)
	for _, sibling := range siblingKeys {
		q.Add("key", sibling)
	}
	resp, err := client.Get(this.Host + "/me?" + q.Encode())
	if err != nil {
		return nil, err
	}
	if resp.StatusCode != http.StatusOK {
		return nil, ErrUnauthorised
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	var user User
	if err := json.Unmarshal(body, &user); err != nil {
		return nil, err
	}

	for _, app := range user.Apps {
		if app.Id == this.Id {
			user.Permissions = app.Permissions
			break
		}
	}

	this.user = &user
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

func getClient(c *http.Cookie, host string) (*http.Client, error) {
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

	return &http.Client{Jar: jar}, nil
}
