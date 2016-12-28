"""Provide client for the Auth service."""

import grpc

from auth_pb2 import (EssenceAuthStub, Empty, App, AppList, AppChange,
                      AppUserRequest, Membership, Group, GroupList,
                      GroupChange, Permission, PermissionValue, User,
                      UserList, UserChange)


__all__ = ['get_client', 'gen_app_user_request', 'Empty', 'App',
           'AppList', 'AppChange', 'AppUserRequest', 'Membership',
           'Group', 'GroupList', 'GroupChange', 'Permission',
           'PermissionValue', 'User', 'UserList', 'UserChange']


class AuthException(Exception):
    def __init__(self, message, code):
        super(AuthException, self).__init__(message)
        self.code = code


def get_client(address):
    """Get an auth serivce client."""
    channel = grpc.insecure_channel(address)
    stub = EssenceAuthStub(channel)
    return stub


def gen_app_user_request(app_id, app_keys, cookies):
    """Helper function do generate an application user request.

    Needs and application ID, the application keys and a cookie
    dictionary from a user request.
    """
    # cookies is expected to be a dict
    try:
        jwt = cookies['ea']
    except KeyError:
        raise AuthException('Unauthorized user', 401)

    return AppUserRequest(ID=app_id, Keys=app_keys, JWT=jwt)
