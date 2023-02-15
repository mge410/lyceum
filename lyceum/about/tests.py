from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self) -> None:
        response = Client().get('/about/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            f'Expected: {HTTPStatus.IM_A_TEAPOT}, '
            f'got: {response.status_code}, testcase: "/about/" ',
        )
