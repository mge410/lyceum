from http import HTTPStatus

from catalog.models import Category, Item, Tag
from django.core import exceptions
from django.test import Client, TestCase
from parameterized import parameterized


class StaticURLTests(TestCase):
    def test_catalog_list_endpoint(self) -> None:
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.expand(
        [
            # OK/200
            ['1', (HTTPStatus.OK,)],
            ['9', (HTTPStatus.OK,)],
            ['0', (HTTPStatus.OK,)],
            ['999239', (HTTPStatus.OK,)],
            ['012', (HTTPStatus.OK,)],
            ['01', (HTTPStatus.OK,)],
            ['010', (HTTPStatus.OK,)],
            ['100', (HTTPStatus.OK,)],
            ['10', (HTTPStatus.OK,)],
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
            ['12', (HTTPStatus.OK,)],
            ['999239', (HTTPStatus.OK,)],
            ['100', (HTTPStatus.OK,)],
            ['10', (HTTPStatus.OK,)],
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
            ['1', (HTTPStatus.OK,)],
            ['999239', (HTTPStatus.OK,)],
            ['100', (HTTPStatus.OK,)],
            ['10', (HTTPStatus.OK,)],
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


class ModelItemTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-slug',
        )

        cls.tag = Tag.objects.create(
            name='Тестовый тэг',
            slug='test-tag-slug',
        )

    @parameterized.expand(
        [
            ['GроGскGошноG'],
            ['прево_схо-дно'],
            ['!! пре1восх-одно !!'],
            ['GGРоСкООООшНоGG!!'],
        ]
    )
    def test_unable_create_to_text(self, text: str) -> None:
        item_count = Item.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.item = Item(
                name='Тестовый товар',
                category=self.category,
                text=f'{text}',
            )
            self.item.full_clean()
            self.item.save()

        self.assertEqual(
            Item.objects.count(),
            item_count,
        )

    @parameterized.expand(
        [
            ['роскошно'],
            ['превосходно '],
            ['!! превосходно !!'],
            ['GGРоСкОшНоGG!!'],
        ]
    )
    def test_create_items_to_text(self, text: str) -> None:
        item_count = Item.objects.count()
        self.item = Item(
            name='Тестовый товар',
            category=self.category,
            text=f'{text}',
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelItemTests.tag)
        self.assertEqual(
            Item.objects.count(),
            item_count + 1,
        )


class ModelTagTests(TestCase):
    @parameterized.expand(
        [
            ['GроGскGошноG'],
            ['прево_схо-дно'],
            ['превосходно'],
            ['!! пре1восх-одно !!'],
            ['GGРоСкООООшНоGG!!'],
            ['testTES1РT'],
            ['te st'],
        ]
    )
    def test_unable_create_to_slug(self, slug: str) -> None:
        tag_count = Tag.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.tag = Tag(
                name='test',
                slug=f'{slug}',
            )
            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(
            Tag.objects.count(),
            tag_count,
            f'slug: {slug} Значение должно состоять только '
            f'из латинских букв, цифр, знаков подчеркивания или дефиса.',
        )

    @parameterized.expand(
        [
            ['testsdf'],
            ['test_one'],
            ['-_test-two_-'],
            ['-_-_--_-'],
        ]
    )
    def test_create_items_to_text(self, slug: str) -> None:
        tag_count = Tag.objects.count()
        self.tag = Tag(
            name='test',
            slug=f'{slug}',
        )
        self.tag.full_clean()
        self.tag.save()
        self.assertEqual(
            Tag.objects.count(),
            tag_count + 1,
            f'slug: {slug} Значение должно состоять только '
            f'из латинских букв, цифр, знаков подчеркивания или дефиса.',
        )


class ModelCategoryTests(TestCase):
    @parameterized.expand(
        [
            ['GроGскGошноG'],
            ['прево_схо-дно'],
            ['превосходно'],
            ['!! пре1восх-одно !!'],
            ['GGРоСкООООшНоGG!!'],
            ['testTES1РT'],
            ['te st'],
        ]
    )
    def test_unable_create_to_slug(self, slug: str) -> None:
        tag_count = Category.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.tag = Category(
                name='test',
                slug=f'{slug}',
            )
            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(
            Category.objects.count(),
            tag_count,
            f'slug: {slug} Значение должно состоять '
            f'только из латинских букв, цифр, знаков '
            f'подчеркивания или дефиса.',
        )

    @parameterized.expand(
        [
            ['testsdf'],
            ['test_one'],
            ['-_test-two_-'],
            ['-_-_--_-'],
        ]
    )
    def test_create_items_to_text(self, slug: str) -> None:
        tag_count = Category.objects.count()
        self.tag = Category(
            name='test',
            slug=f'{slug}',
        )
        self.tag.full_clean()
        self.tag.save()
        self.assertEqual(
            Category.objects.count(),
            tag_count + 1,
            f'slug: {slug} Значение должно состоять только '
            f'из латинских букв, цифр, знаков подчеркивания или дефиса.',
        )
