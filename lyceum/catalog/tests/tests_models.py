from catalog.models import Category, Item, Tag
from django.core import exceptions
from django.test import TestCase
from parameterized import parameterized


class ModelTests(TestCase):
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
        self.item.tags.add(ModelTests.tag)
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

    @parameterized.expand(
        [
            '1',
            '0',
            '123',
            '32767',
        ]
    )
    def test_category_weight_validator(self, weight: str) -> None:
        category_count = Category.objects.count()
        self.category = Category(
            name='Тестов категория',
            weight=f'{weight}',
            slug='test',
        )
        self.category.full_clean()
        self.category.save()
        self.assertEqual(
            Category.objects.count(),
            category_count + 1,
        )

    @parameterized.expand(
        [
            '-01',
            '-1',
            '-123',
            '3276734',
            '31!',
            '3 164',
            'sdfsdf',
        ]
    )
    def test_category_weight_negative_validator(self, weight: str) -> None:
        category_count = Category.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.category = Category(
                name='Тестов категория',
                weight=f'{weight}',
                slug='testS',
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(
            Category.objects.count(),
            category_count,
            f'{weight}',
        )

    @parameterized.expand(
        [
            ['cat', 'сat1'],
            ['cat', 'Cats'],
            ['cat', 'Cat and dog'],
            ['cat', 'Tac '],
            ['cat', 'My cats'],
            ['cat', 'cAAt'],
            ['cat', 'Ccat'],
        ]
    )
    def test_category_keywords_validator(self, name: str, second_name: str) -> None:
        category_count = Category.objects.count()
        self.category = Category(
            name=f'{name}',
            slug='testS',
        )
        self.category.full_clean()
        self.category.save()
        self.category = Category(
            name=f'{second_name}',
            slug='testS2',
        )
        self.category.full_clean()
        self.category.save()

        self.assertEqual(
            Category.objects.count(),
            category_count + 2,
            f'{name}',
        )

    @parameterized.expand(
        [
            ['cat', 'сat'],
            ['cat', 'cat'],
            ['cat', 'Cat'],
            ['cat', 'cat '],
            ['cat', 'cat '],
            ['cat', 'cat !!'],
            ['cat', 'cat !!'],
        ]
    )
    def test_category_keywords_negative_validator(self, name: str, second_name: str) -> None:
        category_count = Category.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.category = Category(
                name=f'{name}',
                slug='testS',
            )
            self.category.full_clean()
            self.category.save()

            self.category = Category(
                name=f'{second_name}',
                slug='testS2',
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(
            Category.objects.count(),
            category_count + 1,
            f'{name}',
        )

    @parameterized.expand(
        [
            ['cat', 'сat'],
            ['cat', 'cat'],
            ['cat', 'Cat'],
            ['cat', 'cat '],
            ['cat', 'cat '],
            ['cat', 'cat !!'],
            ['cat', 'cat !!'],
        ]
    )
    def test_tag_keywords_negative_validator(self, name: str, second_name: str) -> None:
        tag_count = Tag.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.tag = Tag(
                name=f'{name}',
                slug='testS',
            )
            self.tag.full_clean()
            self.tag.save()

            self.tag = Tag(
                name=f'{second_name}',
                slug='testS2',
            )
            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(
            Tag.objects.count(),
            tag_count + 1,
            f'{name}',
        )
