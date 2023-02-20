from django.core import validators
from django.db import models


class NamedBaseModel(models.Model):
    name = models.CharField('Имя', max_length=150)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name[:15]


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True


class SluggedBaseModel(models.Model):
    slug = models.CharField(
        'Символьный код',
        max_length=200,
        unique=True,
        validators=[
            validators.validate_slug,
        ],
    )

    class Meta:
        abstract = True
