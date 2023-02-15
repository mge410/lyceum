from http import HTTPStatus

from django.test import Client, TestCase
from parameterized import parameterized


class StaticURLTests(TestCase):
    @parameterized.expand(
        [
            # OK/200/MOVED_PERMANENTLY/301
            ['/catalog/', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
        ]
    )
    def test_catalog_list_endpoint(self, url, status):
        response = Client().get(f'{url}')
        self.assertIn(response.status_code, status)

    @parameterized.expand(
        [
            # OK/200/MOVED_PERMANENTLY/301
            ['1', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['9', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['0', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['999239', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['012', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['01', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['010', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['100', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['10', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            # 404/NOT_FOUND
            ['-0', (HTTPStatus.NOT_FOUND,)],
            ['-1', (HTTPStatus.NOT_FOUND,)],
            ['10.5', (HTTPStatus.NOT_FOUND,)],
            ['aboba', (HTTPStatus.NOT_FOUND,)],
            ['1C_CALL', (HTTPStatus.NOT_FOUND,)],
            ['sd12', (HTTPStatus.NOT_FOUND,)],
            ['^...1', (HTTPStatus.NOT_FOUND,)],
            ['1^...', (HTTPStatus.NOT_FOUND,)],
            ['1^', (HTTPStatus.NOT_FOUND,)],
            ['11.0', (HTTPStatus.NOT_FOUND,)],
            ['12$', (HTTPStatus.NOT_FOUND,)],
            ['%12', (HTTPStatus.NOT_FOUND,)],
            ['12 %', (HTTPStatus.NOT_FOUND,)],
        ]
    )
    def test_catalog_detail_endpoint(self, test_case, status):
        response = Client().get(f'/catalog/{test_case}/')
        self.assertIn(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: {test_case}',
        )

    @parameterized.expand(
        [
            # OK/200/MOVED_PERMANENTLY/301
            ['1', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['12', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['999239', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['100', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['10', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            # 404/NOT_FOUND
            ['-0', (HTTPStatus.NOT_FOUND,)],
            ['-1', (HTTPStatus.NOT_FOUND,)],
            ['01', (HTTPStatus.NOT_FOUND,)],
            ['010', (HTTPStatus.NOT_FOUND,)],
            ['0', (HTTPStatus.NOT_FOUND,)],
            ['012', (HTTPStatus.NOT_FOUND,)],
            ['aboba', (HTTPStatus.NOT_FOUND,)],
            ['1C_CALL', (HTTPStatus.NOT_FOUND,)],
            ['sd12', (HTTPStatus.NOT_FOUND,)],
            ['^...1', (HTTPStatus.NOT_FOUND,)],
            ['1^...', (HTTPStatus.NOT_FOUND,)],
            ['1^', (HTTPStatus.NOT_FOUND,)],
            ['11.0', (HTTPStatus.NOT_FOUND,)],
            ['12$', (HTTPStatus.NOT_FOUND,)],
            ['%12', (HTTPStatus.NOT_FOUND,)],
            ['12 %', (HTTPStatus.NOT_FOUND,)],
        ]
    )
    def test_catalog_detail_re_endpoint(self, test_case, status):
        response = Client().get(f'/catalog/re/{test_case}')
        self.assertIn(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: {test_case}',
        )

    @parameterized.expand(
        [
            # OK/200/MOVED_PERMANENTLY/301
            ['1', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['1', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['999239', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['100', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            ['10', (HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY)],
            # 404/NOT_FOUND
            ['-0', (HTTPStatus.NOT_FOUND,)],
            ['-1', (HTTPStatus.NOT_FOUND,)],
            ['01', (HTTPStatus.NOT_FOUND,)],
            ['010', (HTTPStatus.NOT_FOUND,)],
            ['0', (HTTPStatus.NOT_FOUND,)],
            ['012', (HTTPStatus.NOT_FOUND,)],
            ['aboba', (HTTPStatus.NOT_FOUND,)],
            ['1C_CALL', (HTTPStatus.NOT_FOUND,)],
            ['sd12', (HTTPStatus.NOT_FOUND,)],
            ['12$', (HTTPStatus.NOT_FOUND,)],
            ['%12', (HTTPStatus.NOT_FOUND,)],
            ['12 %', (HTTPStatus.NOT_FOUND,)],
        ]
    )
    def test_catalog_detail_converter_endpoint(self, test_case, status):
        response = Client().get(f'/catalog/converter/{test_case}')
        self.assertIn(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: {test_case}',
        )
