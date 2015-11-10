import requests


class App(object):

    def __init__(self, host, id, key):
        self.host = host
        self.id = id
        self.key = key
        self.user = None

    def get_user(self, cookies, sibling_keys=None):
        if self.user is not None:
            return self.user

        # cookies is expected to be a dict
        cookie = {'essence_auth': cookies['essence_auth']}

        keys = sibling_keys.append(self.key) if sibling_keys is not None else self.key
        query_string = {'key': keys}

        response = requests.get('{}/me'.format(self.host), params=query_string, cookies=cookie)
        user = response.json()

        return user
