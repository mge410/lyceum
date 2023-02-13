from django.test import Client, TestCase
from http import HTTPStatus


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
