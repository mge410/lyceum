from django.test import Client
from django.test import TestCase
import django.urls


class ModelsTests(TestCase):
    def test_feedback_context(self):
        response = Client().get(
            django.urls.reverse(
                'feedback:feedback',
            )
        )
        self.assertIn('form', response.context)

    def test_feedback_success_redirect_context(self):
        form_value = {
            'email': 'fff@mail.com',
            'text': '123',
        }

        response = Client().post(
            django.urls.reverse(
                'feedback:feedback',
            ),
            data=form_value,
        )

        self.assertRedirects(
            response, django.urls.reverse('feedback:feedback')
        )
