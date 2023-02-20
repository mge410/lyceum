from django.db import models


class AbstractModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)
    name = models.CharField('Имя', max_length=150)

    class Meta:
        abstract = True
