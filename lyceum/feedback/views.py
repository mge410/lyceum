from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
import django.http
import django.shortcuts
import feedback.forms as forms
from feedback.models import FeedbackFiles


def feedback(request: django.http.HttpRequest) -> django.http.HttpResponse:
    template = 'feedback/feedback.html'

    feedback_form = forms.FeedbackForm(request.POST or None)
    feedback_user_data_form = forms.FeedbackDataUserForm(request.POST or None)
    feedback_files_form = forms.FeedbackFilesForm(
        request.POST, request.FILES or None
    )

    context = {
        'feedback_form': feedback_form,
        'feedback_user_data_form': feedback_user_data_form,
        'feedback_files_form': feedback_files_form,
    }

    if feedback_form.is_valid() and feedback_user_data_form.is_valid():
        send_mail(
            'Feedback',
            f'Thanks for the feedback <br> Your message '
            f'- « {feedback_form.cleaned_data["text"]} »',
            settings.MAIL_SENDER,
            [f'{feedback_user_data_form.cleaned_data["email"]}'],
            fail_silently=False,
        )

        messages.success(
            request, 'Thank you for the confidential communication =)'
        )

        data_user = feedback_user_data_form.save(commit=False)
        feedback = feedback_form.save()

        data_user.feedback = feedback
        data_user.save()

        if feedback_files_form.is_valid():
            for file in request.FILES.getlist('files'):
                feedback_files = FeedbackFiles(
                    feedback=feedback,
                    files=file,
                )
                feedback_files.save()

        return django.shortcuts.redirect('feedback:feedback')

    return django.shortcuts.render(request, template, context)
