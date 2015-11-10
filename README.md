# lib-essence-auth
Clients for the Essence auth service

## Go

```go
import (
    auth "github.com/essence-tech/lib-essence-auth/"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    app := auth.App{
        Id: "apps-secret-id",
        Key: "apps-secret-key",
        Host: "auth-service-host",
    }

    user, err := app.GetUser(r)
    if err != nil {
        panic(err)
    }

    ...
}
```

## Python
Install from pip with
```
pip install git+git://github.com/essence-tech/lib-essence-auth.git@master
```

```python
import essenceauth

...

    app = App("auth-service-host", "apps-secret-id", "apps-secret-key")
    user = app.get_user(dict_of_cookies)

...
```
