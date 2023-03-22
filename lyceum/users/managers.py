from django.contrib.auth.models import User
from django.db import models

import users.models


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return (
            super(UserProfileManager, self)
            .get_queryset()
            .select_related('profile')
            .filter(is_active=True)
        )

    def get_user_list(self):
        return self.get_queryset().only(
            User.username.field.name,
            User.email.field.name,
        )

    def get_user_detail(self):
        return self.get_queryset().only(
            'username', 'email', 'profile__image',
            'first_name', 'last_name',
            'profile__coffee_count', 'profile__birthday'
        )
