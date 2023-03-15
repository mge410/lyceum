from django import forms
from feedback.models import Feedback
from feedback.models import FeedbackDataUser
from feedback.models import FeedbackFiles


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            Feedback.text.field.name,
        ]

        labels = {
            Feedback.text.field.name: 'Message *',
        }

        help_texts = {
            Feedback.text.field.name: 'Write'
            ' what you think about'
            ' our company =)',
        }


class FeedbackFilesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FeedbackFilesForm, self).__init__(*args, **kwargs)
        self.fields[FeedbackFiles.files.field.name].required = False

    class Meta:
        model = FeedbackFiles
        fields = [
            FeedbackFiles.files.field.name,
        ]

        widgets = {
            FeedbackFiles.files.field.name: forms.ClearableFileInput(
                attrs={
                    'multiple': True,
                },
            )
        }


class FeedbackDataUserForm(forms.ModelForm):
    class Meta:
        model = FeedbackDataUser
        fields = [
            FeedbackDataUser.email.field.name,
        ]

        labels = {
            FeedbackDataUser.email.field.name: 'Email *',
        }

        help_texts = {
            FeedbackDataUser.email.field.name: 'Enter your email',
        }
