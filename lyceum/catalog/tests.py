from parameterized import parameterized
from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_list_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.expand(
        [
            [1, HTTPStatus.OK],
            [9, HTTPStatus.OK],
            [0, HTTPStatus.OK],
            [999239, HTTPStatus.OK],
            ['012', HTTPStatus.OK],
            ['aboba', HTTPStatus.NOT_FOUND],
            ['1C_CALL', HTTPStatus.NOT_FOUND],
            ['sd12', HTTPStatus.NOT_FOUND],
            ['12$', HTTPStatus.NOT_FOUND],
        ]
    )
    def test_catalog_detail_endpoint(self, test_case, status) -> None:
        response = Client().get(f'/catalog/{test_case}')
        self.assertEqual(
            response.status_code,
            status,
            f'Expected: {status}, got: {response.status_code}, testcase: {test_case}',
        )

    @parameterized.expand(
        [
            [1, HTTPStatus.OK],
            [1, HTTPStatus.OK],
            [999239, HTTPStatus.OK],
            [0, HTTPStatus.NOT_FOUND],
            ['012', HTTPStatus.NOT_FOUND],
            ['aboba', HTTPStatus.NOT_FOUND],
            ['1C_CALL', HTTPStatus.NOT_FOUND],
            ['sd12', HTTPStatus.NOT_FOUND],
            ['12$', HTTPStatus.NOT_FOUND],
        ]
    )
    def test_catalog_detail_re_endpoint(self, test_case, status) -> None:
        response = Client().get(f'/catalog/re/{test_case}')
        self.assertEqual(
            response.status_code,
            status,
            f'Expected: {status}, got: {response.status_code}, testcase: {test_case}',
        )

    @parameterized.expand(
        [
            [12, HTTPStatus.OK],
            [93, HTTPStatus.OK],
            [999239, HTTPStatus.OK],
            [0, HTTPStatus.NOT_FOUND],
            ['012', HTTPStatus.NOT_FOUND],
            ['aboba', HTTPStatus.NOT_FOUND],
            ['1C_CALL', HTTPStatus.NOT_FOUND],
            ['sd12', HTTPStatus.NOT_FOUND],
            ['12$', HTTPStatus.NOT_FOUND],
        ]
    )
    def test_catalog_detail_converter_endpoint(self, test_case, status) -> None:
        response = Client().get(f'/catalog/converter/{test_case}')
        self.assertEqual(
            response.status_code,
            status,
            f'Expected: {status}, got: {response.status_code}, testcase: {test_case}',
        )
