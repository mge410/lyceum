from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)
