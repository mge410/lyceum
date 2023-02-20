from django.db import models


class NamedBaseModel(models.Model):
    name = models.CharField('Имя', max_length=150, unique=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name[:15]


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True


class SluggedBaseModel(models.Model):
    slug = models.SlugField(
        'Символьный код',
        max_length=200,
        unique=True,
    )

    class Meta:
        abstract = True
