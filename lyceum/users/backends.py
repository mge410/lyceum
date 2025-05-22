from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpRequest
from django.utils import timezone


class AuthBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, user_id: int) -> None:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

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

    def authenticate(
        self, request: HttpRequest, username: str, password: str
    ) -> None | User:
        try:
            user = User.objects.get(
                Q(username=username) | Q(email=AuthBackend.normalize_email(username))
            )
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        user.profile.login_failed_count += 1
        if user.profile.login_failed_count == settings.NUMBER_OF_LOGIN_ATTEMPTS:
            user.is_active = False
            user.profile.freezing_account_data = timezone.now()
            send_mail(
                "Account recovery link",
                "http://127.0.0.1:8000/auth/recovery/" f"{user.username}",
                settings.MAIL_SENDER,
                [f"{user.email}"],
                fail_silently=False,
            )
            user.save()
        user.profile.save()
        return None
