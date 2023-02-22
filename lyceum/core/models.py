from django.db import models


class NamedBaseModel(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        help_text='Максимум 150 символов. Можно использовать'
        ' только буквы цифры и знаки подчеркивания и тире.',
        verbose_name='название',
    )

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
        help_text='Максимум 200 символов. Можно использовать'
        ' только буквы цифры и знаки подчеркивания и тире.',
        verbose_name='символьный код',
    )

    class Meta:
        abstract = True
