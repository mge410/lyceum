import django.forms
import feedback.models


class FeedbackForm(django.forms.Form):
    email = django.forms.EmailField(
        label='Email *', help_text='Enter your email'
    )
    text = django.forms.CharField(
        label='Message *',
        help_text='Write what you think about our company =)',
    )
    files = django.forms.FileField(
        required=False,
        label='Files',
        help_text='Download file',
    )

    def save(self, file_list):
        data = self.cleaned_data

        feedback_data = feedback.models.Feedback(text=data['text'])
        data_user = feedback.models.FeedbackUserData(
            email=data['email'], feedback=feedback_data
        )

        feedback_data.save()
        data_user.save()

        if data['files'] is not None:
            for file in file_list:
                feedback_files = feedback.models.FeedbackFiles(
                    files=file, feedback=feedback_data
                )
                feedback_files.save()
