import datetime

from django.http import HttpRequest

from users.models import UserProfileProxy


def birthday_people(request: HttpRequest) -> dict:
    try:
        today_user_datetime = datetime.date(
            *map(int, request.COOKIES.get('django_timezone').split('-'))
        )
    except Exception:
        today_user_datetime = datetime.datetime.now().date()

    return {
        'birthday_users': UserProfileProxy.objects.get_birthday_list(
            today_user_datetime
        )
    }
