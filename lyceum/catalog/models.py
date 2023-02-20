from catalog.validators import perfect_validator
from core.models import NamedBaseModel, PublishedBaseModel, SluggedBaseModel
from django.db import models


class Category(NamedBaseModel, PublishedBaseModel, SluggedBaseModel):
    weight = models.SmallIntegerField('Вес', default=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(NamedBaseModel, PublishedBaseModel, SluggedBaseModel):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Item(NamedBaseModel, PublishedBaseModel):
    text = models.TextField(
        'Описание',
        help_text='Опишите товар',
        validators=[perfect_validator('роскошно', 'превосходно')],
    )

    category = models.ForeignKey(
        'category',
        on_delete=models.PROTECT,
        related_name='catalog_items',
        verbose_name='Категория',
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тэги',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.name[:20]
