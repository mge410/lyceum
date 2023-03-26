import os
import shutil

import django.urls
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from feedback.models import Feedback, FeedbackFiles


@override_settings(MEDIA_ROOT=os.path.join(settings.MEDIA_ROOT, 'test_media'))
class ViewsTests(TestCase):
    def setUp(self):
        self.feedback_data_with_files = {
            'text': '123',
            'email': 'aboba@ma.ru',
            'files': [
                SimpleUploadedFile('file.txt', b'aboba'),
                SimpleUploadedFile('file2.txt', b'aboba2'),
            ],
        }
        super(ViewsTests, self).setUp()

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

    def test_attach_files_in_feedback(self):
        response = Client().post(
            reverse('feedback:feedback'),
            self.feedback_data_with_files,
            follow=True,
        )

        self.assertEquals(response.status_code, 200)

    def test_attach_files_in_feedback_models(self):
        file_count = FeedbackFiles.objects.count()

        Client().post(
            reverse('feedback:feedback'),
            self.feedback_data_with_files,
            follow=True,
        )

        self.assertEquals(
            file_count + len(self.feedback_data_with_files['files']),
            FeedbackFiles.objects.count(),
        )

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

    def tearDown(self):
        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)
            super(ViewsTests, self).tearDown()
