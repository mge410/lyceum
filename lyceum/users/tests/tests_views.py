import datetime

from django.contrib.auth.models import User
from django.core import exceptions
from django.test import Client
from django.test import override_settings
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import mock
from parameterized import parameterized
import pytz


class RegisterViewsTests(TestCase):
    user_register_data = {
        'username': 'ABEBRA',
        'email': 'aboba@ma.ru',
        'password1': '123123123g',
        'password2': '123123123g',
    }

    def test_user_register_context(self):
        response = Client().get(
            reverse(
                'users:register',
            )
        )
        self.assertIn('form', response.context)

    def test_user_register_success_redirect(self):
        response = Client().post(
            reverse('users:register'),
            self.user_register_data,
            follow=True,
        )

        self.assertRedirects(response, reverse('homepage:home'))

    def test_user_register_success(self):
        user_count = User.objects.count()

        Client().post(
            reverse('users:register'),
            self.user_register_data,
            follow=True,
        )

        self.assertEqual(User.objects.count(), user_count + 1)

    @override_settings(DEFAULT_USER_ACTIVITY='False')
    def test_register_is_active_false(self):
        Client().post(
            reverse('users:register'),
            self.user_register_data,
            follow=True,
        )

        user = User.objects.get(username=self.user_register_data['username'])

        self.assertFalse(user.is_active)

    @override_settings(DEFAULT_USER_ACTIVITY='True')
    def test_register_is_active_true(self):
        Client().post(
            reverse('users:register'),
            self.user_register_data,
            follow=True,
        )

        user = User.objects.get(username=self.user_register_data['username'])

        self.assertTrue(user.is_active)

    @override_settings(DEFAULT_USER_ACTIVITY='False')
    def test_user_activate_success(self):
        Client().post(
            reverse('users:register'),
            self.user_register_data,
            follow=True,
        )

        user = User.objects.get(username=self.user_register_data['username'])

        Client().get(
            reverse('users:activate', args=(user.username,)),
            follow=True,
        )

        user = User.objects.get(username=self.user_register_data['username'])

        self.assertTrue(user.is_active)

    @override_settings(DEFAULT_USER_ACTIVITY='False')
    @mock.patch('django.utils.timezone.now')
    def test_user_activate_error(self, mock_now):
        Client().post(
            reverse('users:register'),
            self.user_register_data,
            follow=True,
        )

        user = User.objects.get(username=self.user_register_data['username'])

        utc = pytz.UTC
        mock_now.return_value = utc.localize(
            timezone.datetime.now() + datetime.timedelta(hours=12)
        )

        Client().get(
            reverse('users:activate', args=(user.username,)),
            follow=True,
        )

        with self.assertRaises(exceptions.ObjectDoesNotExist):
            User.objects.get(username=self.user_register_data['username'])

    @parameterized.expand(
        [
            [
                user_register_data['username'],
                user_register_data['password1'],
            ],
        ],
    )
    def test_user_login_username(self, username, password):
        Client().post(
            reverse('users:register'),
            self.user_register_data,
            follow=True,
        )

        user = User.objects.get(username=username)
        last_login = user.last_login

        Client().post(
            reverse('users:login'),
            {
                'username': username,
                'password': password,
            },
            follow=True,
        )

        user = User.objects.get(username=username)
        now_login = user.last_login
        self.assertTrue(last_login != now_login)

    @parameterized.expand(
        [
            ['aboba@ya.ru', 'aboba@yandex.ru'],
            ['ABOBA@yA.ru', 'aboba@yandex.ru'],
            ['abo.ba.+ger@gmail.com', 'aboba@gmail.com'],
            ['ABo.ba.+ger@gmail.com', 'aboba@gmail.com'],
        ]
    )
    def test_user_normalize_email(self, email: str, expected: str) -> None:
        """тестируем блокировку пользователя"""
        Client().post(
            reverse('users:register'),
            {
                'username': self.user_register_data['username'],
                'email': email,
                'password1': self.user_register_data['password1'],
                'password2': self.user_register_data['password2'],
            },
            follow=True,
        )
        user = User.objects.get(pk=1)
        self.assertEqual(user.email, expected)

    @override_settings(DEFAULT_USER_ACTIVITY='True')
    def test_user_to_success_block(self) -> None:
        """тестируем валидацию почты"""

        Client().post(
            reverse('users:register'),
            {
                'username': self.user_register_data['username'],
                'email': self.user_register_data['email'],
                'password1': self.user_register_data['password1'],
                'password2': self.user_register_data['password2'],
            },
            follow=True,
        )

        for i in range(5):
            Client().post(
                reverse('users:login'),
                {
                    'username': self.user_register_data['username'],
                    'password': '1',
                },
                follow=True,
            )

        user = User.objects.get(username=self.user_register_data['username'])
        self.assertFalse(user.is_active)

    @override_settings(DEFAULT_USER_ACTIVITY='True')
    def test_user_to_success_recovery(self) -> None:
        """тестируем восстановление пользователя"""
        Client().post(
            reverse('users:register'),
            {
                'username': self.user_register_data['username'],
                'email': self.user_register_data['email'],
                'password1': self.user_register_data['password1'],
                'password2': self.user_register_data['password2'],
            },
            follow=True,
        )

        for i in range(5):
            Client().post(
                reverse('users:login'),
                {
                    'username': self.user_register_data['username'],
                    'password': '1',
                },
                follow=True,
            )

        Client().get(
            reverse(
                'users:recovery',
                kwargs={'name': self.user_register_data['username']},
            ),
        )

        user = User.objects.get(username=self.user_register_data['username'])
        self.assertTrue(user.is_active)
