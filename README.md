# lib-essence-auth
Clients for the Essence auth service

## Go

```go
import (
    "net/http"

    "github.com/essence-tech/lib-essence-auth/"
)

func handler(w http.ResponseWriter, r *http.Request) {
    authService := essenceauth.New("auth-service-host")

    // TODO
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
