import re

from django.core.exceptions import ValidationError
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


class KeywordsBaseModel(models.Model):
    class Meta:
        abstract = True

    def clean(self, *args, **kwargs):
        keywords = self.get_keywords(self.name.lower())
        keywords_list = [
            item.keywords for item in self.__class__.objects.all()
        ]
        if keywords in keywords_list:
            raise ValidationError(
                'Уже есть обьект с похожем названием.'
                ' Перефразируйте ваш обьект или воспользуйтесь существующим'
            )
        self.keywords = keywords
        super(KeywordsBaseModel, self).clean()

    keywords = models.CharField(
        max_length=150,
        help_text='Ключевые слова',
        verbose_name='ключевые слова',
        editable=False,
    )

    def get_keywords(self, text: str) -> str:
        replace_letters = {
            'e': 'е',
            'o': 'о',
            'c': 'с',
            'x': 'х',
            'a': 'а',
        }
        for key in replace_letters.keys():
            text = text.replace(key, replace_letters[key])
            keyword_list = sorted(filter(None, re.split(r'\W', text)))
        return ','.join(keyword_list)
