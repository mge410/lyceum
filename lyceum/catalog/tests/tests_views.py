from django.forms.models import model_to_dict
from django.test import Client
from django.test import TestCase
import django.urls
from parameterized import parameterized

from catalog.models import Category
from catalog.models import Item
from catalog.models import Tag


class ModelsTests(TestCase):
    fixtures = ["data.json"]

    def test_homepage_correct_context(self):
        response = Client().get(django.urls.reverse("homepage:home"))
        items = response.context["items"]
        self.assertEqual(items.count(), 4)

    def test_catalog_list_correct_context(self):
        response = Client().get(django.urls.reverse("catalog:item_list"))
        items = response.context["items"]
        self.assertEqual(items.count(), 6)

    def test_catalog_detail_context(self):
        response = Client().get(
            django.urls.reverse(
                "catalog:item_detail",
                args=[Item.objects.filter(is_published=True)[:1][0].id],
            )
        )
        self.assertIn("item", response.context)

    @parameterized.expand(
        [
            [
                "id",
            ],
            [
                "name",
            ],
            [
                "text",
            ],
            [
                "category",
            ],
            [
                "tags",
            ],
        ]
    )
    def test_catalog_list_attributes(self, field):
        context_item = model_to_dict(
            Client().get(django.urls.reverse("catalog:item_list")).context["items"][0]
        )
        self.assertIn(field, context_item.keys())

    @parameterized.expand(
        [
            [
                "created_at",
            ],
            [
                "updated_at",
            ],
        ]
    )
    def test_catalog_detail_list_attributes(self, field):
        context_item = model_to_dict(
            Client().get(django.urls.reverse("catalog:item_list")).context["items"][0]
        )
        self.assertNotIn(field, context_item.keys())

    @parameterized.expand(
        [
            [
                "id",
            ],
            [
                "name",
            ],
            [
                "text",
            ],
            [
                "category",
            ],
            [
                "tags",
            ],
        ]
    )
    def test_catalog_detail_attributes(self, field):
        context_item = model_to_dict(
            Client()
            .get(
                django.urls.reverse(
                    "catalog:item_detail",
                    args=[Item.objects.filter(is_published=True)[:1][0].id],
                )
            )
            .context[0]["item"]
        )
        self.assertIn(field, context_item.keys())

    @parameterized.expand(
        [
            [
                "created_at",
            ],
            [
                "updated_at",
            ],
        ]
    )
    def test_catalog_detail_bad_attributes(self, field):
        context_item = model_to_dict(
            Client()
            .get(
                django.urls.reverse(
                    "catalog:item_detail",
                    args=[Item.objects.filter(is_published=True)[:1][0].id],
                )
            )
            .context[0]["item"]
        )
        self.assertNotIn(field, context_item.keys())

    def tearDown(self) -> None:
        Item.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()

        super(ModelsTests, self).tearDown()
