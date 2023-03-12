from django.test import TestCase
from feedback.forms import FeedbackForm


class FeedbackTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_text_label(self):
        text_label = FeedbackTests.form.fields['text'].label
        self.assertEquals(text_label, 'Message *')

    def test_email_label(self):
        email_label = FeedbackTests.form.fields['email'].label
        self.assertEquals(email_label, 'Email *')

    def test_text_help_text(self):
        text_help_text = FeedbackTests.form.fields['text'].help_text
        self.assertEquals(
            text_help_text, 'Write what you think about our company =)'
        )

    def test_email_help_text(self):
        email_help_text = FeedbackTests.form.fields['email'].help_text
        self.assertEquals(email_help_text, 'Enter your email')
