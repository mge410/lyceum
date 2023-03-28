from datetime import datetime, timedelta
from random import sample

import catalog.models
from django.db import models
from django.db.models import F, Prefetch


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
            .order_by(
                f'{catalog.models.Item.category.field.name}'
                f'__{catalog.models.Category.name.field.name}'
            )
        )

    def new_item_list(self):
        try:
            my_ids = list(
                catalog.models.Item.objects.filter(
                    is_published=True,
                    created_at__range=(
                        datetime.now() - timedelta(days=7),
                        datetime.now(),
                    ),
                ).values_list(
                    f'{catalog.models.Item.id.field.name}', flat=True
                )
            )
            if len(my_ids) < 5:
                my_ids_count = len(my_ids)
            else:
                my_ids_count = 5
            if my_ids is None:
                return None
            return (
                self.prefetch_to_items()
                .filter(
                    id__in=sample(my_ids, my_ids_count),
                    created_at__range=(
                        datetime.now() - timedelta(days=7),
                        datetime.now(),
                    ),
                    is_published=True,
                    category__is_published=True,
                )
                .order_by(f'{catalog.models.Item.name.field.name}')[:5]
            )
        except Exception:
            return None

    def friday_item_list(self):
        return (
            self.prefetch_to_items()
            .filter(
                updated_at__week_day=6,
                is_published=True,
                category__is_published=True,
            )
            .order_by(f'-{catalog.models.Item.created_at.field.name}')[:5]
        )

    def unchecked_item_list(self):
        return (
            self.prefetch_to_items()
            .filter(
                updated_at=F(f'{catalog.models.Item.created_at.field.name}'),
                is_published=True,
                category__is_published=True,
            )
            .order_by(
                f'{catalog.models.Item.category.field.name}'
                f'__{catalog.models.Category.name.field.name}'
            )
        )

    def catalog_detail(self):
        return (
            self.prefetch_to_items()
            .prefetch_related(
                Prefetch(
                    f'{catalog.models.Item.gallery_images.rel.related_name}',
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
            .select_related(
                f'{catalog.models.Item.category.field.name}',
                f'{catalog.models.Item.main_image.related.related_name}',
            )
            .prefetch_related(
                Prefetch(
                    f'{catalog.models.Item.tags.field.name}',
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True
                    ).only(f'{catalog.models.Tag.name.field.name}'),
                )
            )
            .only(
                catalog.models.Item.name.field.name,
                catalog.models.Item.text.field.name,
                f'{catalog.models.Item.category.field.name}'
                f'__{catalog.models.Category.name.field.name}',
                f'{catalog.models.Item.main_image.related.related_name}'
                f'__{catalog.models.MainImageItem.image.field.name}',
            )
        )
