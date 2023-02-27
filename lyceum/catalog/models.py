from catalog.validators import ValidateMustContain
import core.models as core
from django.core import validators
from django.db import models


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
        Category,
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


class MainImageItem(core.NamedBaseModel, core.ImageBaseModel):
    items = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='галерея изображение',
    )

    class Meta:
        verbose_name = 'главная картинка'
        verbose_name_plural = 'главные изображения'
        default_related_name = 'main_image'


class GalleryImagesItem(core.NamedBaseModel, core.ImageBaseModel):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='главное изображение',
    )

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'галерея изображений'
        default_related_name = 'gallery_images'
