from catalog.managers import ItemManager
import core.models as core
from django.core import validators
from django.db import models


class Category(
    core.NamedBaseModel,
    core.PublishedBaseModel,
    core.SluggedBaseModel,
    core.NormalizedNameBaseModel,
):
    weight = models.PositiveSmallIntegerField(
        'weight',
        default=100,
        validators=[
            validators.MinValueValidator(0, 'Minimum number to enter 0'),
            validators.MaxValueValidator(
                32767, 'The maximum number to enter is 32767'
            ),
        ],
        help_text='Enter weight please',
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        default_related_name = 'category'


class Tag(
    core.NamedBaseModel,
    core.PublishedBaseModel,
    core.SluggedBaseModel,
    core.NormalizedNameBaseModel,
):
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        default_related_name = 'tags'


class Item(
    core.NamedBaseModel,
    core.PublishedBaseModel,
    core.CreatedDateBaseModel,
    core.UpdatedDateBaseModel,
    core.TextBaseModel,
):
    objects = ItemManager()

    is_on_main = models.BooleanField(
        'show on homepage', default=False, help_text='Show on homepage'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='category',
        help_text='The product must have a category.',
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name='tags',
        help_text='The element must have at least 1 tag.',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        default_related_name = 'items'

    def __str__(self) -> str:
        return self.name[:20]


class MainImageItem(core.NamedBaseModel, core.ImageBaseModel):
    def saving_path(self, name):
        return f'uploads/main_image/{self.items.id}/{name}'

    items = models.OneToOneField(
        Item,
        verbose_name='main image',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='Enter main image please',
    )

    image = models.ImageField(
        'main image',
        upload_to=saving_path,
        help_text='Will be rendered at 300px',
    )

    class Meta:
        verbose_name = 'main image'
        verbose_name_plural = 'main images'
        default_related_name = 'main_image'


class GalleryImagesItem(core.NamedBaseModel, core.ImageBaseModel):
    def saving_path(self, name):
        return f'uploads/gallery_images/{self.item.id}/{name}'

    image = models.ImageField(
        'main image',
        upload_to=saving_path,
        help_text='Will be rendered at 300px',
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='gallery images',
        help_text='gallery images',
    )

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'image gallery'
        default_related_name = 'gallery_images'
