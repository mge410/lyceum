from http import HTTPStatus

from django.test import Client, TestCase
from parameterized import parameterized


class StaticURLTests(TestCase):
    @parameterized.expand(
        [
            # OK/200/MOVED_PERMANENTLY/301
            ['/', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['/coffee/', (HTTPStatus.IM_A_TEAPOT,)],
        ]
    )
    def test_homepage_endpoint_status(self, url, status):
        response = Client().get(f'{url}')
        self.assertIn(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: {url} ',
        )

    @parameterized.expand(
        [
            # OK/200/MOVED_PERMANENTLY/301
            ['/coffee/', '<div>Я чайник</div>'],
        ]
    )
    def test_coffee_endpoint_text(self, url, text):
        response = Client().get(f'{url}')
        self.assertEqual(
            response.content.decode('utf-8'),
            f'{text}',
            f'Expected: "{text}", '
            f'got: {response.content.decode("utf-8")}, testcase: {url} ',
        )
