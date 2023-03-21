from django.contrib.auth.models import User
from django.db import models


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return (
            super(UserProfileManager, self)
            .get_queryset()
            .select_related(User.profile.related.related_name)
            .filter(is_active=True)
        )
