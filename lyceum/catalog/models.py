from django.core import validators
from django.db import models

import core.models as core
from catalog.validators import ValidateMustContain


class Category(
    core.NamedBaseModel,
    core.PublishedBaseModel,
    core.SluggedBaseModel,
    core.KeywordsBaseModel,
):
    weight = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='вес',
        validators=[
            validators.MinValueValidator(0, 'Минимальное число для ввода 0'),
            validators.MaxValueValidator(
                32767, 'Максимальное число для ввода 32767'
            ),
        ],
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Tag(
    core.NamedBaseModel,
    core.PublishedBaseModel,
    core.SluggedBaseModel,
    core.KeywordsBaseModel,
):
    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'
        default_related_name = 'tags'


class Item(core.NamedBaseModel, core.PublishedBaseModel):
    text = models.TextField(
        validators=[ValidateMustContain('роскошно', 'превосходно')],
        help_text='В тексте должно быть одно из слов: роскошно, превосходно.',
        verbose_name='описание',
    )

    category = models.ForeignKey(
        'category',
        on_delete=models.PROTECT,
        help_text='У предмета должна быть категория.',
        verbose_name='категория',
    )

    tags = models.ManyToManyField(
        Tag,
        help_text='У предмета должн быть хотя бы 1 тэг.',
        verbose_name='тэги',
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        default_related_name = 'items'

    def __str__(self) -> str:
        return self.name[:20]
