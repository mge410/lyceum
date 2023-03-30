import datetime

from django.http import HttpRequest

from users.models import UserProfileProxy


def birthday_people(request: HttpRequest) -> dict:
    if request.COOKIES.get('django_timezone'):
        return {
            'birthday_users': UserProfileProxy.objects.get_birthday_list(
                datetime.date(
                    *map(
                        int, request.COOKIES.get('django_timezone').split('-')
                    )
                )
            )
        }
    return {
        'birthday_users': UserProfileProxy.objects.get_birthday_list(
            today_user_datetime=datetime.datetime.now().date()
        )
    }
