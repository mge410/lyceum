from catalog.models import Category, Item, Tag
from django.core import exceptions
from django.test import TestCase
from parameterized import parameterized


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
            ['GG1РоСкООООшНоGG!!'],
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
            f'{text}',
        )

    @parameterized.expand(
        [
            ['роскошно'],
            ['превосходно '],
            ['!! превосходно !!'],
            ['G РоСкОшНо GG!!'],
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
        )
