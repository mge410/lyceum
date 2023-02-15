from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self) -> None:
        response = Client().get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_coffee_endpoint(self) -> None:
        response = Client().get('/coffee/')
        self.assertContains(
            response, 'Я чайник', status_code=HTTPStatus.IM_A_TEAPOT
        )
