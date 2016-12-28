"""Test auth service client."""

import unittest

from essenceauth import (gen_app_user_request, user_has_permission,
                         AuthException, User, App, Permission, PermissionValue)


class TestClient(unittest.TestCase):

    def setUp(self):
        pass

    def test_gen_app_user_request(self):
        req = gen_app_user_request('id', 'key', {'ea': 'jwt'})

        self.assertEqual(req.ID, 'id')
        self.assertEqual(req.Keys, ['key'])
        self.assertEqual(req.JWT, 'jwt')

        self.assertRaises(
            AuthException,
            gen_app_user_request,
            'id',
            'key',
            {'not_the_cookie': 'jwt'})

    def test_user_has_permission(self):
        user = User(Apps=[App(ID='1', Permissions=[Permission(ID='p1')])])
        self.assertEqual(user_has_permission(user, '1', 'p1'), True)
        self.assertEqual(user_has_permission(user, '1', 'p2'), False)
        self.assertEqual(user_has_permission(user, '2', 'p1'), False)


if __name__ == '__main__':
    unittest.main()
