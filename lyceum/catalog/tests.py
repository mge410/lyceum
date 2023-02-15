from http import HTTPStatus

from django.test import Client, TestCase
from parameterized import parameterized


class StaticURLTests(TestCase):
    def test_catalog_list_endpoint(self) -> None:
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.expand(
        [
            ['1', HTTPStatus.OK],
            ['9', HTTPStatus.OK],
            ['0', HTTPStatus.OK],
            ['999239', HTTPStatus.OK],
            ['012', HTTPStatus.OK],
            ['01', HTTPStatus.OK],
            ['010', HTTPStatus.OK],
            ['100', HTTPStatus.OK],
            ['10', HTTPStatus.OK],
            ['-0', HTTPStatus.NOT_FOUND],
            ['-1', HTTPStatus.NOT_FOUND],
            ['10.5', HTTPStatus.NOT_FOUND],
            ['aboba', HTTPStatus.NOT_FOUND],
            ['1C_CALL', HTTPStatus.NOT_FOUND],
            ['sd12', HTTPStatus.NOT_FOUND],
            ['^...1', HTTPStatus.NOT_FOUND],
            ['1^...', HTTPStatus.NOT_FOUND],
            ['1^', HTTPStatus.NOT_FOUND],
            ['11.0', HTTPStatus.NOT_FOUND],
            ['12$', HTTPStatus.NOT_FOUND],
            ['%12', HTTPStatus.NOT_FOUND],
            ['12 %', HTTPStatus.NOT_FOUND],
        ]
    )
    def test_catalog_detail_endpoint(self, test_case, status) -> None:
        response = Client().get(f'/catalog/{test_case}/')
        self.assertEqual(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: {test_case}',
        )

    @parameterized.expand(
        [
            ['1', HTTPStatus.OK],
            ['12', HTTPStatus.OK],
            ['999239', HTTPStatus.OK],
            ['100', HTTPStatus.OK],
            ['10', HTTPStatus.OK],
            ['-0', HTTPStatus.NOT_FOUND],
            ['-1', HTTPStatus.NOT_FOUND],
            ['01', HTTPStatus.NOT_FOUND],
            ['010', HTTPStatus.NOT_FOUND],
            ['0', HTTPStatus.NOT_FOUND],
            ['012', HTTPStatus.NOT_FOUND],
            ['aboba', HTTPStatus.NOT_FOUND],
            ['1C_CALL', HTTPStatus.NOT_FOUND],
            ['sd12', HTTPStatus.NOT_FOUND],
            ['^...1', HTTPStatus.NOT_FOUND],
            ['1^...', HTTPStatus.NOT_FOUND],
            ['1^', HTTPStatus.NOT_FOUND],
            ['11.0', HTTPStatus.NOT_FOUND],
            ['12$', HTTPStatus.NOT_FOUND],
            ['%12', HTTPStatus.NOT_FOUND],
            ['12 %', HTTPStatus.NOT_FOUND],
        ]
    )
    def test_catalog_detail_re_endpoint(self, test_case, status) -> None:
        response = Client().get(f'/catalog/re/{test_case}')
        self.assertEqual(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: {test_case}',
        )

    @parameterized.expand(
        [
            ['1', HTTPStatus.OK],
            ['1', HTTPStatus.OK],
            ['999239', HTTPStatus.OK],
            ['100', HTTPStatus.OK],
            ['10', HTTPStatus.OK],
            ['-0', HTTPStatus.NOT_FOUND],
            ['-1', HTTPStatus.NOT_FOUND],
            ['01', HTTPStatus.NOT_FOUND],
            ['010', HTTPStatus.NOT_FOUND],
            ['0', HTTPStatus.NOT_FOUND],
            ['012', HTTPStatus.NOT_FOUND],
            ['aboba', HTTPStatus.NOT_FOUND],
            ['1C_CALL', HTTPStatus.NOT_FOUND],
            ['sd12', HTTPStatus.NOT_FOUND],
            ['12$', HTTPStatus.NOT_FOUND],
            ['%12', HTTPStatus.NOT_FOUND],
            ['12 %', HTTPStatus.NOT_FOUND],
        ]
    )
    def test_catalog_detail_converter_endpoint(
        self, test_case, status
    ) -> None:
        response = Client().get(f'/catalog/converter/{test_case}')
        self.assertEqual(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: {test_case}',
        )
