from http import HTTPStatus

from django.test import Client
from django.test import TestCase
from parameterized import parameterized
from catalog.models import Item
from catalog.models import Category


class StaticURLTests(TestCase):
    def setUp(self) -> None:
        self.base_category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-slug',
        )
        self.item = Item.objects.create(
            name='Тестовый тэг',
            category=self.base_category,
            text='превосходно',
        )
        self.item = Item.objects.create(
            name='Тестовый тэг2',
            category=self.base_category,
            text='превосходно!',
        )
        super(StaticURLTests, self).setUp()

    def test_catalog_list_endpoint(self) -> None:
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.expand(
        [
            # OK/200
            ['1', (HTTPStatus.OK,)],
            ['2', (HTTPStatus.OK,)],
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
    def test_catalog_detail_endpoint(
        self, test_case: str, status: tuple
    ) -> None:
        response = Client().get(f'/catalog/{test_case}/')
        self.assertIn(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: {test_case}',
        )

    @parameterized.expand(
        [
            # OK/200
            ['1', (HTTPStatus.OK,)],
            ['2', (HTTPStatus.OK,)],
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
    def test_catalog_detail_re_endpoint(
        self, test_case: str, status: tuple
    ) -> None:
        response = Client().get(f'/catalog/re/{test_case}/')
        self.assertIn(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: {test_case}',
        )

    @parameterized.expand(
        [
            # OK/200
            ['1', (HTTPStatus.OK,)],
            ['2', (HTTPStatus.OK,)],
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
    def test_catalog_detail_converter_endpoint(
        self, test_case: str, status: tuple
    ) -> None:
        response = Client().get(f'/catalog/converter/{test_case}/')
        self.assertIn(
            response.status_code,
            status,
            f'Expected: {status}, '
            f'got: {response.status_code}, testcase: {test_case}',
        )

    def tearDown(self) -> None:
        Item.objects.all().delete()
        Category.objects.all().delete()

        super(StaticURLTests, self).tearDown()
