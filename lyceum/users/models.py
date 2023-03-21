import core.models
from django.contrib.auth.models import User
from django.db import models
from users.managers import UserProfileManager


class Profile(core.models.ImageBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birthday = models.DateField(
        'birthday', blank=True, null=True, help_text='Enter date of birth'
    )

    image = models.ImageField(
        'profile picture',
        upload_to='uploads/user_image/',
        blank=True,
        null=True,
        help_text='Enter profile picture',
    )

    coffee_count = models.BigIntegerField(
        'coffee count',
        default=0,
        help_text='Number of user requests for coffee',
    )

    class Meta:
        verbose_name = 'additional field'
        verbose_name_plural = 'additional fields'
        default_related_name = 'profile'


class UserProfileProxy(User):
    objects = UserProfileManager()

    class Meta:
        proxy = True
        ordering = (User.date_joined.field.name,)
