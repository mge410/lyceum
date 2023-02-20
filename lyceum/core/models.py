from django.db import models


class NamedBaseModel(models.Model):
    name = models.CharField('название', max_length=150, unique=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name[:15]


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField('опубликовано', default=True)

    class Meta:
        abstract = True


class SluggedBaseModel(models.Model):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='символьный код',
    )

    class Meta:
        abstract = True
