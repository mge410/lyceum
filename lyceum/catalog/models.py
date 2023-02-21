from catalog.validators import perfect_validator
from core.models import NamedBaseModel, PublishedBaseModel, SluggedBaseModel
from django.core import validators
from django.db import models


class Category(NamedBaseModel, PublishedBaseModel, SluggedBaseModel):
    weight = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='вес',
        validators=[
            validators.MinValueValidator(
                0, 'Минимальное число для ввода 0'
            ),
            validators.MaxValueValidator(
                32767, 'Максимальное число для ввода 32767'
            )
        ],
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
        validators=[perfect_validator('роскошно', 'превосходно')],
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
