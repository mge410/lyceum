from django.contrib.auth.models import User
from django.core import exceptions
from django.test import Client
from django.test import override_settings
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import mock
import pytz


class ViewsTests(TestCase):
    def setUp(self):
        self.user_register_data = {
            'username': 'ABEBRA',
            'email': 'aboba@ma.ru',
            'password1': '123123123g',
            'password2': '123123123g',
        }
        super(ViewsTests, self).setUp()

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
        mail_count = User.objects.count()

        Client().post(
            reverse('users:register'),
            self.user_register_data,
            follow=True,
        )

        self.assertEqual(User.objects.count(), mail_count + 1)

    @override_settings(DEFAULT_USER_ACTIVITY='False')
    def test_register_is_active_false(self):
        Client().post(
            reverse('users:register'),
            self.user_register_data,
            follow=True,
        )

        user = User.objects.get(username=self.user_register_data['username'])

        self.assertEqual(user.is_active, False)

    @override_settings(DEFAULT_USER_ACTIVITY='True')
    def test_register_is_active_true(self):
        Client().post(
            reverse('users:register'),
            self.user_register_data,
            follow=True,
        )

        user = User.objects.get(username=self.user_register_data['username'])

        self.assertEqual(user.is_active, True)

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

        self.assertEqual(user.is_active, True)

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
        mock_now.return_value = utc.localize(timezone.datetime(2025, 1, 3))

        Client().get(
            reverse('users:activate', args=(user.username,)),
            follow=True,
        )

        with self.assertRaises(exceptions.ObjectDoesNotExist):
            User.objects.get(username=self.user_register_data['username'])

    def tearDown(self):
        super(ViewsTests, self).tearDown()
