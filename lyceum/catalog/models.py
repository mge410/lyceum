from Core.models import AbstractModel, perfect_validate
from django.core import validators
from django.db import models


class Category(AbstractModel):
    slug = models.CharField(
        'Символьный код',
        max_length=200,
        unique=True,
        validators=[validators.validate_slug],
    )
    weight = models.SmallIntegerField('Вес', default=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name[:15]


class Tag(AbstractModel):
    slug = models.CharField(
        'Символьный код',
        max_length=200,
        unique=True,
        validators=[
            validators.validate_slug,
        ],
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self) -> str:
        return self.name[:15]


class Item(AbstractModel):
    text = models.TextField(
        'Описание', help_text='Опишите товар', validators=[perfect_validate]
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
        return self.text[:15]
