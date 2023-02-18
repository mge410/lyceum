from http import HTTPStatus

from django.test import Client, TestCase
from parameterized import parameterized


class StaticURLTests(TestCase):
    def test_homepage_endpoint_status(self) -> None:
        response = Client().get('/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            f'Expected: {HTTPStatus.OK}, '
            f'got: {response.status_code}, testcase: / ',
        )

    def test_home_coffee_endpoint_status(self) -> None:
        response = Client().get('/coffee/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.IM_A_TEAPOT,
            f'Expected: {HTTPStatus.IM_A_TEAPOT}, '
            f'got: {response.status_code}, testcase: /coffee/ ',
        )

    @parameterized.expand(
        [
            # OK/200
            ['/coffee/', '<div>Я чайник</div>'],
        ]
    )
    def test_coffee_endpoint_text(self, url: str, text: str) -> None:
        response = Client().get(f'{url}')
        self.assertEqual(
            response.content.decode('utf-8'),
            f'{text}',
            f'Expected: "{text}", '
            f'got: {response.content.decode("utf-8")}, testcase: {url} ',
        )
