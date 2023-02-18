from django.db import models


class AbstractModel(models.Model):
    is_published = models.BooleanField(default=True)
    name = models.CharField(max_length=150)

    class Meta:
        abstract = True
