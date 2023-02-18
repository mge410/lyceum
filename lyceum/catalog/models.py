from Core.models import AbstractModel
from django.core import validators
from django.db import models


class Category(AbstractModel):
    slug = models.CharField(
        max_length=200,
        unique=True,
        validators=[
            validators.validate_slug,
        ],
    )
    weight = models.SmallIntegerField()


class Tag(AbstractModel):
    slug = models.CharField(
        max_length=200,
        unique=True,
        validators=[
            validators.validate_slug,
        ],
    )


class Item(AbstractModel):
    text = models.TextField()

    category = models.ForeignKey(
        'category', on_delete=models.PROTECT, related_name='catalog_items'
    )

    tags = models.ManyToManyField(Tag)
