from django import forms
from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            Feedback.email.field.name,
            Feedback.text.field.name,
        )

        labels = {
            Feedback.email.field.name: 'Email *',
            Feedback.text.field.name: 'Message *',
        }

        help_texts = {
            Feedback.email.field.name: 'Enter your email',
            Feedback.text.field.name: 'Write'
            ' what you think about'
            ' our company =)',
        }
