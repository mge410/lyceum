import django.urls

from catalog.models import Category
from catalog.models import Item
from catalog.models import Tag
from django.core import exceptions
from django.test import TestCase, Client
from parameterized import parameterized


class ModelsTests(TestCase):
    def setUp(self) -> None:
        self.base_category_published = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-slug',
        )
        self.base_category_unpublished = Category.objects.create(
            name='Тестовая категория2',
            slug='test-category-slugg',
            is_published=False,
        )
        self.base_tag_published = Tag.objects.create(
            name='Тестовый тэг1',
            slug='test-tag-slug',
        )
        self.base_tag_unpublished = Tag.objects.create(
            name='Тестовый тэг2',
            slug='test-tag-slug2',
            is_published=False,
        )
        self.item_published = Item.objects.create(
            name='Тестовый item1',
            category=self.base_category_published,
            text='превосходно',
        )
        self.item_published_main = Item.objects.create(
            name='Тестовый item12',
            category=self.base_category_published,
            text='превосходно',
            is_on_main=True,
        )
        self.item_unpublished = Item.objects.create(
            name='Тестовый item13',
            category=self.base_category_published,
            text='превосходно!',
            is_published=False,
        )
        self.item_unpublished_category = Item.objects.create(
            name='Тестовый item14',
            category=self.base_category_unpublished,
            text='превосходно',
            is_on_main=True,
        )
        self.item_unpublished_tag = Item.objects.create(
            name='Тестовый item15',
            category=self.base_category_published,
            text='превосходно!',
        )
        self.item_unpublished_tag.tags.add(self.base_tag_unpublished.pk)
        super(ModelsTests, self).setUp()

    def test_homepage_correct_context(self):
        response = Client().get(django.urls.reverse('homepage:home'))
        items = response.context['items']
        self.assertEqual(items.count(), 1)

    def test_catalog_list_correct_context(self):
        response = Client().get(django.urls.reverse('catalog:item_list'))
        items = response.context['items']
        self.assertEqual(items.count(), 3)

    def test_catalog_detail_context(self):
        response = Client().get(django.urls.reverse('catalog:item_detail', args=[self.item_published.id]))
        self.assertIn('item', response.context)

    def tearDown(self) -> None:
        Item.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()

        super(ModelsTests, self).tearDown()
