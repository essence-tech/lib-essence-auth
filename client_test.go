package auth

import (
	"crypto/md5"
	"encoding/hex"
	"testing"

	"gopkg.in/essence-tech/lib-essence-auth.v2/essenceauth"
)

var values = []*essenceauth.PermissionValue{
	&essenceauth.PermissionValue{
		Key:   "pv2",
		Value: "pv2",
	},
	&essenceauth.PermissionValue{
		Key:   "pv1",
		Value: "pv1",
	},
}

var perms = []*essenceauth.Permission{
	&essenceauth.Permission{
		ID:     "p1",
		Name:   "p1",
		Values: values,
	},
}

var apps = []*essenceauth.App{
	&essenceauth.App{
		ID:          "a1",
		Key:         "a1",
		Permissions: perms,
	},
}

func TestPermissionSetID(t *testing.T) {
	_str := "p1_pv1|pv1:pv2|pv2"
	_md5 := md5.Sum([]byte(_str))
	expected := hex.EncodeToString(_md5[:])

	u := &essenceauth.User{
		Apps: apps,
	}

	out := PermissionSetID(u)
	if out != expected {
		t.Error(out)
		t.Error(expected)
	}

	out2 := PermissionSetID(u)
	if out != out2 {
		t.Error(out)
		t.Error(out2)
	}
}

func TestUserHasPermission(t *testing.T) {
	u := &essenceauth.User{
		Apps: apps,
	}

	if !UserHasPermission(u, "a1", "p1") {
		t.Error("Should be true")
	}

	if UserHasPermission(u, "a1", "p2") {
		t.Error("Should be false")
	}

	if UserHasPermission(u, "a2", "p1") {
		t.Error("Should be false")
	}
}
