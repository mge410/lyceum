from django.contrib.auth.models import User
from django.db import models

import core.models
from users.managers import UserProfileManager


class Profile(core.models.ImageBaseModel):
    def saving_path(self, name: str) -> str:
        return f"uploads/user_image/{self.user.id}/{name}"

    login_failed_count = models.PositiveSmallIntegerField(
        "number of failed logins",
        default=0,
        help_text="number of failed logins",
    )

    account_blocking_date = models.DateTimeField(
        "account blocking date",
        default=None,
        null=True,
        blank=True,
        help_text="Account lockout date",
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="user",
        help_text="user",
    )

    birthday = models.DateField(
        "birthday", blank=True, null=True, help_text="Enter date of birth"
    )

    image = models.ImageField(
        "profile picture",
        upload_to=saving_path,
        blank=True,
        null=True,
        help_text="Enter profile picture",
    )

    coffee_count = models.PositiveSmallIntegerField(
        "coffee count",
        default=0,
        help_text="Number of user requests for coffee",
    )

    class Meta:
        verbose_name = "additional field"
        verbose_name_plural = "additional fields"
        default_related_name = "profile"


class UserProfileProxy(User):
    objects = UserProfileManager()

    class Meta:
        proxy = True
        ordering = (User.date_joined.field.name,)
