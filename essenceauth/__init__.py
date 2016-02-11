import requests
import json

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AuthException(Exception):
    def __init__(self, message, code):
        super(AuthException, self).__init__(message)
        self.code = code


class App(object):
    ''' Represents the application
    '''
    def __init__(self, host, id, key):
        self.host = host
        self.id = id
        self.key = key
        self.user = None

    def get_user(self, cookies, sibling_keys=None):
        ''' Returns a user object by using the users
            cookies. Throws on authentication error
        '''
        if self.user is not None:
            return self.user

        # cookies is expected to be a dict
        try:
            cookie = {'essence_auth': cookies['essence_auth']}
        except KeyError:
            raise AuthException('Unauthorized user', 401)

        # Gather all keys
        keys = sibling_keys.append(self.key) if sibling_keys is not None else self.key
        query_string = {'key': keys}
        logging.debug(query_string)

        response = requests.get('{}/me2'.format(self.host), params=query_string, cookies=cookie)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise AuthException('Unauthorized user', err.response.status_code)

        user = User(self, response.json())
        self.user = user
        return user

    def set_permissions(self, *permissions):
        data = json.dumps(permissions, cls=PermissionEncoder)
        response = requests.post(
            '{}/api/v1/apps/{}'.format(self.host, self.id),
            params={'key': self.key},
            data=data,
            allow_redirects=False)
        response.raise_for_status()

        if response.status_code != 200:
            raise AuthException('Something went wrong. Check URL', response.status_code)



class Permission(object):
    ''' An application permission
    '''
    def __init__(self, id, name, values):
        self.id = id
        self.name = name
        self.values = values

    @staticmethod
    def from_api(api_response):
        try:
            values = api_response['values']
        except KeyError:
            values = None

        return Permission(
            api_response['id'],
            api_response['name'],
            values)


class PermissionEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Permission):
            return o.__dict__
        return super(PermissionEncoder, self).default(o)


class User(object):
    ''' Representation of a user from the auth service
    '''
    def __init__(self, host_app, api_response):
        self.name = api_response['name']
        self.email = api_response['email']
        self.permissions = []

        for app in api_response['apps']:
            if app['id'] == host_app.id:
                try:
                    self.permissions.extend([Permission.from_api(perm) for perm in app['permissions']])
                except KeyError as err:
                    logging.error(err)
                    logging.warning('User: No permissions for app {}'.format(host_app.id))
                    self.permissions = None
                    continue

        try:
            self.picture = api_response['picture']
        except KeyError:
            self.picture = None

    def has_permission(self, id):
        if self.permissions is None:
            return False

        for perm in self.permissions:
            if perm.id == id:
                return True

        return False

