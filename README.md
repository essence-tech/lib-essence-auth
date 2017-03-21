# lib-essence-auth
Clients for the Essence auth service. Client code can be generated using the Makefile.

## Go

```go
import (
    "net/http"

    "gopkg.in/essence-tech/lib-essence-auth.v2"
    "gopkg.in/essence-tech/lib-essence-auth.v2/essenceauth"
    "golang.org/x/net/context"
)

func handler(w http.ResponseWriter, r *http.Request) {
    service := auth.New("auth-service-host")
    defer service.Close()

    req := auth.GenAppUserRequest("app-id", []string{"app-key"}, r)
    user, err := service.AppGetUser(context.Background(), req)
    if user.Email == "" || err != nil {
        // No user returned *or* an error occured.
    }

    // User is ready for use.
    ...
}
```

## Python
Install from pip with
```
pip install git+git://github.com/essence-tech/lib-essence-auth.git@grpc-auth
```

```python
import essenceauth


client = essenceauth.get_client('host_addr:port')

req = essenceauth.gen_app_user_request('app-id', 'app-key', dict_of_cookies')
user = client.AppGetUser(req)

# Mosts other calls require a JWT token..
client.ListApps(essenceauth.Empty(), metadata=[(b'authorization', b'your.jwt.token')])

# or for example
response = client.ListUsers(essenceauth.Empty(), metadata=[(b'authorization', b'your.jwt.token')])

for u in response.Users:
    print(u)

```
