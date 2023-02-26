import core.models as core
from catalog.validators import ValidateMustContain
from django.core import validators
from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe


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


class MainImageItem(core.NamedBaseModel):
    image = models.ImageField('Будут приведены к 300px',
                              upload_to='catalog/',
                              )

    def get_image_300x300(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="50">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'Main'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'главная картинка'
        verbose_name_plural = 'главные изображения'
        default_related_name = 'items'


class Item(core.NamedBaseModel, core.PublishedBaseModel):
    text = models.TextField(
        validators=[ValidateMustContain('роскошно', 'превосходно')],
        help_text='В тексте должно быть одно из слов: роскошно, превосходно.',
        verbose_name='описание',
    )

    main_image = models.OneToOneField(MainImageItem, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Главное изображение', related_name='item')

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
