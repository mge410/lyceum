import re
from typing import Any

from core.validators import ValidateMustContain
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import mark_safe
from pytils import translit
from sorl.thumbnail import get_thumbnail


class NamedBaseModel(models.Model):
    name = models.CharField(
        'name',
        max_length=150,
        unique=True,
        help_text='Maximum 150 characters. '
        'Only letters, numbers, underscores,'
        ' and dashes can be used.',
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name[:15]


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField('published', default=True)

    class Meta:
        abstract = True


class SluggedBaseModel(models.Model):
    slug = models.SlugField(
        'slug',
        max_length=200,
        unique=True,
        help_text='Maximum 200 characters. '
        'Only letters, numbers, underscores,'
        ' and dashes can be used.',
    )

    class Meta:
        abstract = True


class TextBaseModel(models.Model):
    text = models.TextField(
        'description',
        validators=[ValidateMustContain('luxuriously', 'excellent')],
        help_text='The text should contain '
        'one of the words: luxuriously,'
        ' excellent.',
    )

    class Meta:
        abstract = True


class TextMessageModel(models.Model):
    text = models.TextField(
        'message to us',
        help_text='Message to us',
    )

    class Meta:
        abstract = True


class CreatedDateBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedDateBaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ImageBaseModel(models.Model):
    image = models.ImageField(
        'Will be rendered at 300px',
        upload_to='catalog/',
    )

    class Meta:
        abstract = True

    def get_image_300x300(self) -> str:
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def image_tmb(self) -> str:
        if self.image:
            return mark_safe(f'<img src="{self.get_image_300x300().url}">')
        return 'No picture'

    def save(self, *args: Any, **kwargs: Any) -> None:
        if self.image is None:
            self.image.name = '.'.join(
                list(
                    map(
                        lambda x: translit.slugify(x),
                        self.image.name.split('.'),
                    )
                )
            )
            super().save(*args, **kwargs)
            self.image = self.get_image_300x300()
        else:
            super().save(*args, **kwargs)

    image_tmb.short_description = 'Image'


class NormalizedNameBaseModel(models.Model):
    normalized_name = models.CharField(
        'normalized name',
        max_length=150,
        editable=False,
        null=True,
        help_text='Normalized name',
    )

    class Meta:
        abstract = True

    def clean(self, *args: Any, **kwargs: Any) -> None:
        normalized_name = self.get_normalized_name(self.name)
        normalized_name_list = [
            item.normalized_name for item in self.__class__.objects.all()
        ]
        if normalized_name in normalized_name_list:
            raise ValidationError(
                'An object with the same name '
                'already exists. Rephrase your '
                'object or use an existing one'
            )
        self.normalized_name = normalized_name
        super(NormalizedNameBaseModel, self).clean()

    def get_normalized_name(self, text: str) -> str:
        replace_letters = {
            'е': 'e',
            'о': 'o',
            'с': 'c',
            'х': 'x',
            'а': 'a',
            'р': 'p',
            'у': 'y',
            'А': 'A',
            'Р': 'P',
            'С': 'C',
            'Е': 'E',
            'О': 'O',
            'Х': 'X',
            'Т': 'T',
            'М': 'M',
            'К': 'K',
            'В': 'B',
            'Н': 'H',
        }
        for key in replace_letters.keys():
            text = text.replace(key, replace_letters[key])
            normalized_name = re.sub(r'\W', '', text).lower()
        return normalized_name
