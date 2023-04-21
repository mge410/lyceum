from django.test import TestCase

from feedback.forms import FeedbackForm


class FeedbackTests(TestCase):
    def setUp(self) -> None:
        self.feedback_form = FeedbackForm()
        super(FeedbackTests, self).setUp()

    def test_text_label(self) -> None:
        text_label = self.feedback_form['text'].label
        self.assertEquals(text_label, 'Message *')

    def test_email_label(self) -> None:
        email_label = self.feedback_form['email'].label
        self.assertEquals(email_label, 'Email *')

    def test_text_help_text(self) -> None:
        text_help_text = self.feedback_form['text'].help_text
        self.assertEquals(
            text_help_text, 'Write what you think about our company =)'
        )

    def test_email_help_text(self) -> None:
        email_help_text = self.feedback_form.fields['email'].help_text
        self.assertEquals(email_help_text, 'Enter your email')
