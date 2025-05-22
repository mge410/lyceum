from django.contrib.auth.models import User
from django.db import models

from catalog.models import Item
from core.models import CreatedDateBaseModel
from rating.managers import GradeManager


class Grade(CreatedDateBaseModel):
    objects = GradeManager()

    class Rating(models.TextChoices):
        hatred = "1", "hatred"
        dislike = "2", "dislike"
        neutrally = "3", "neutrally"
        adore = "4", "adore"
        love = "5", "love"

    rating = models.CharField(
        "rating",
        max_length=1,
        default=Rating.neutrally,
        choices=Rating.choices,
        blank=True,
        help_text="Items rating",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="user",
        help_text="The user who left the rating",
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name="item",
        help_text="Product that has been rated",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(name="unique_rating", fields=["item", "user"])
        ]
        verbose_name = "rating"
        verbose_name_plural = "ratings"
        default_related_name = "ratings"
