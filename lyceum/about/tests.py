from http import HTTPStatus

from django.test import Client, TestCase
from parameterized import parameterized


class StaticURLTests(TestCase):
    @parameterized.expand(
        [
            # OK/200/MOVED_PERMANENTLY/301
            ['/about/', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            # NOT_FOUND/404
            ['/about/1', (HTTPStatus.NOT_FOUND,)],
        ]
    )
    def test_about_endpoint(self, url: str, status: tuple) -> None:
        response = Client().get(f'{url}')
        self.assertIn(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: "{url}" ',
        )
