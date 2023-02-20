from django.db import models

from catalog.validators import perfect_validator
from core.models import NamedBaseModel, PublishedBaseModel, SluggedBaseModel


class Category(NamedBaseModel, PublishedBaseModel, SluggedBaseModel):
    weight = models.SmallIntegerField(
        default=100,
        verbose_name='вес',
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Tag(NamedBaseModel, PublishedBaseModel, SluggedBaseModel):
    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'


class Item(NamedBaseModel, PublishedBaseModel):
    text = models.TextField(
        help_text='опишите товар',
        validators=[perfect_validator('роскошно', 'превосходно')],
        verbose_name='описание',
    )

    category = models.ForeignKey(
        'category',
        on_delete=models.PROTECT,
        related_name='catalog_items',
        verbose_name='категория',
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name='тэги',
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self) -> str:
        return self.name[:20]
