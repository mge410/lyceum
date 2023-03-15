from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from feedback.forms import FeedbackDataUserForm
from feedback.forms import FeedbackFilesForm
from feedback.forms import FeedbackForm
from feedback.models import FeedbackFiles


def feedback(request: HttpRequest) -> HttpResponse:
    template = 'feedback/feedback.html'

    feedback_form = FeedbackForm(request.POST or None)
    feedback_user_data_form = FeedbackDataUserForm(request.POST or None)
    feedback_files_form = FeedbackFilesForm(
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

        return redirect('feedback:feedback')

    return render(request, template, context)
