from django.test import Client
from django.test import TestCase
import django.urls
from feedback.models import Feedback


class ModelsTests(TestCase):
    def test_feedback_success_save_context(self):
        mail_count = Feedback.objects.count()
        form_data = {
            'email': 'fff@mail.com',
            'text': '123123',
        }

        Client().post(
            django.urls.reverse(
                'feedback:feedback',
            ),
            data=form_data,
        )

        self.assertEqual(Feedback.objects.count(), mail_count + 1)

    def test_feedback_error_save_context(self):
        mail_count = Feedback.objects.count()
        form_data = {
            'email': 'fffmail.com',
            'text': '123123',
        }

        Client().post(
            django.urls.reverse(
                'feedback:feedback',
            ),
            data=form_data,
        )

        self.assertEqual(Feedback.objects.count(), mail_count)
