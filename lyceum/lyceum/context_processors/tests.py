import datetime

import django.urls
from django.test import Client, TestCase

import users.models


class ContextProcessorsTests(TestCase):
    user_register_data = {
        'username': 'ABEBRA',
        'email': 'aboba@ma.ru',
        'password1': '123123123g',
        'password2': '123123123g',
    }

    def test_context_processors_success(self) -> None:
        client = Client()

        test_user = users.models.UserProfileProxy.objects.create_user(
            username=self.user_register_data['username']
        )
        users.models.Profile.objects.create(
            user=test_user, birthday=datetime.datetime.now().date()
        )

        response = client.get(django.urls.reverse('homepage:home'))
        bithday_users = response.context['birthday_users']
        self.assertTrue(bithday_users)

    def test_context_processors_failed(self) -> None:
        client = Client()

        test_user = users.models.UserProfileProxy.objects.create_user(
            username=self.user_register_data['username']
        )
        users.models.Profile.objects.create(
            user=test_user,
            birthday=datetime.datetime.now().date()
            + datetime.timedelta(days=12),
        )

        response = client.get(django.urls.reverse('homepage:home'))
        bithday_users = response.context['birthday_users']
        self.assertFalse(bithday_users)
