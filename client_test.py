"""Test auth service client."""

import unittest

from essenceauth import gen_app_user_request, AuthException


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


if __name__ == '__main__':
    unittest.main()
