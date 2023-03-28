from catalog.models import Item
from core.models import CreatedDateBaseModel
from django.contrib.auth.models import User
from django.db import models
from rating.managers import GradeManager


class Grade(CreatedDateBaseModel):
    objects = GradeManager()

    class Rating(models.TextChoices):
        hatred = '1', 'hatred'
        dislike = '2', 'dislike'
        neutrally = '3', 'neutrally'
        adore = '4', 'adore'
        love = '5', 'love'

    rating = models.CharField(
        'rating',
        max_length=1,
        default=Rating.neutrally,
        choices=Rating.choices,
        help_text='Items rating',
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='user',
        help_text='The user who left the rating',
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='item',
        help_text='Product that has been rated',
        related_name='grades'
    )

    class Meta:
        unique_together = ('user', 'item')
        verbose_name = 'rating'
        verbose_name_plural = 'ratings'
        default_related_name = 'ratings'
