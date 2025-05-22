from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.db.models import QuerySet

import users.models


class UserProfileManager(UserManager):
    def get_queryset(self) -> QuerySet:
        return (
            super(UserProfileManager, self)
            .get_queryset()
            .select_related(f"{User.profile.related.related_name}")
            .filter(is_active=True)
        )

    def get_user_list(self) -> QuerySet:
        return self.get_queryset().only(
            User.username.field.name,
            User.email.field.name,
        )

    def get_birthday_list(self, today_user_datetime: datetime) -> QuerySet:
        return (
            self.get_queryset()
            .only(
                User.username.field.name,
                User.email.field.name,
                f"{User.profile.related.related_name}"
                f"__{users.models.Profile.birthday.field.name}",
            )
            .filter(
                profile__birthday__day=today_user_datetime.day,
                profile__birthday__month=today_user_datetime.month,
                profile__birthday__year__lte=today_user_datetime.year,
            )
        )

    def get_user_detail(self) -> QuerySet:
        return self.get_queryset().only(
            User.username.field.name,
            User.email.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
            f"{User.profile.related.related_name}"
            f"__{users.models.Profile.image.field.name}",
            f"{User.profile.related.related_name}"
            f"__{users.models.Profile.birthday.field.name}",
            f"{User.profile.related.related_name}"
            f"__{users.models.Profile.coffee_count.field.name}",
        )

    @classmethod
    def normalize_email(cls, email: str) -> str:
        if not email:
            return ""
        try:
            email_user, email_domain = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email_user_no_tags = email_user.split("+")[0].lower()
            if email_domain.lower() in ["yandex.ru", "ya.ru"]:
                email_user_no_tags = email_user_no_tags.replace(".", "-")
                email_domain = "yandex.ru"
            if email_domain.lower() == "gmail.com":
                email_user_no_tags = email_user_no_tags.replace(".", "")
            email = "@".join([email_user_no_tags, email_domain.lower()])
        return email
