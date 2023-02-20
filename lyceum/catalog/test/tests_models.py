from django.core import exceptions
from django.test import TestCase
from parameterized import parameterized

from catalog.models import Category, Item, Tag


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
            ['роскошно'],
            ['превосходно '],
            ['!! превосходно !!'],
            ['G РоСкОшНо GG!!'],
            ['Роскошно!'],
            ['Супер (роскошно)'],
            ['превосходно,роскошно'],
        ]
    )
    def test_item_validator(self, text: str) -> None:
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

    @parameterized.expand(
        [
            ['GроGскGошноG'],
            ['прево_схо-дно'],
            ['!! пре1восх-одно !!'],
            ['GG1РоСкООООшНоGG!!'],
            ['роскошноGGG'],
            ['йлцорудыфвпревосходнойцуйцлур'],
            ['роскошно111'],
            ['нероскошно'],
        ]
    )
    def test_item_negative_validator(self, text: str) -> None:
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
