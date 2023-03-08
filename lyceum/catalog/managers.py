import catalog.models
from django.db import models
from django.db.models import Prefetch


class ItemManager(models.Manager):
    def homepage(self):
        return self.prefetch_to_items().filter(
            is_published=True,
            is_on_main=True,
            category__is_published=True,
        )

    def catalog_list(self):
        return (
            self.prefetch_to_items()
            .filter(
                is_published=True,
                category__is_published=True,
            )
            .order_by('category__name')
        )

    def new_item_list(self):
        return (
            self.prefetch_to_items()
            .filter(
                is_published=True,
                category__is_published=True,
            )
            .order_by('category__name')
        )

    def catalog_detail(self):
        return (
            self.prefetch_to_items()
            .prefetch_related(
                Prefetch(
                    'gallery_images',
                )
            )
            .filter(
                is_published=True,
                category__is_published=True,
            )
        )

    def prefetch_to_items(self):
        return (
            self.get_queryset()
            .select_related('category', 'main_image')
            .prefetch_related(
                Prefetch(
                    'tags',
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True
                    ).only('name'),
                )
            )
            .only(
                catalog.models.Item.name.field.name,
                catalog.models.Item.text.field.name,
                f'{catalog.models.Item.category.field.name}'
                f'__{catalog.models.Category.name.field.name}',
                f'main_image__{catalog.models.MainImageItem.image.field.name}',
            )
        )
