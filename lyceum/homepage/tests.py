from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint_status(self) -> None:
        response = Client().get('/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            f'Expected: {HTTPStatus.OK}, '
            f'got: {response.status_code}, testcase: "/" ',
        )

    def test_coffee_endpoint_status(self) -> None:
        response = Client().get('/coffee/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.IM_A_TEAPOT,
            f'Expected: {HTTPStatus.IM_A_TEAPOT}, '
            f'got: {response.status_code}, testcase: "/coffee/" ',
        )

    def test_coffee_endpoint_text(self) -> None:
        response = Client().get('/coffee/')
        self.assertEqual(
            response.content.decode('utf-8'),
            '<div>Я чайник</div>',
            f'Expected: "<div>Я чайник</div>", '
            f'got: {response.content.decode("utf-8")}, testcase: "/coffee/" ',
        )
