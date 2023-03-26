import parameterized.parameterized
from django.test import Client, TestCase
from django.urls import reverse


class StaticUrlsTests(TestCase):
    @parameterized.parameterized.expand(
        [
            ('login', 200),
            ('password_reset', 200),
            ('password_reset_complete', 200),
            ('password_reset_done', 200),
            ('register', 200),
            ('logout', 200),
            ('password_change_done', 302),
        ]
    )
    def test_registration_endpoints(self, url, status):
        response = Client().get(reverse(f'users:{url}'))
        self.assertEqual(response.status_code, status)

    def test_users_endpoints(self):
        response = Client().get(reverse('users:users_list'))
        self.assertEqual(response.status_code, 200)
