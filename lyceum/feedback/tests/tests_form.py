from django.test import TestCase
from feedback.forms import FeedbackDataUserForm
from feedback.forms import FeedbackForm


class FeedbackTests(TestCase):
    def setUp(self):
        self.feedback_form = FeedbackForm()
        self.feedback_form_user = FeedbackDataUserForm()

        super(FeedbackTests, self).setUp()

    def test_text_label(self):
        text_label = self.feedback_form.fields['text'].label
        self.assertEquals(text_label, 'Message *')

    def test_email_label(self):
        email_label = self.feedback_form_user.fields['email'].label
        self.assertEquals(email_label, 'Email *')

    def test_text_help_text(self):
        text_help_text = self.feedback_form.fields['text'].help_text
        self.assertEquals(
            text_help_text, 'Write what you think about our company =)'
        )

    def test_email_help_text(self):
        email_help_text = self.feedback_form_user.fields['email'].help_text
        self.assertEquals(email_help_text, 'Enter your email')
