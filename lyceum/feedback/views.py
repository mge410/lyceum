from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
import django.http
import django.shortcuts
import feedback.forms as forms


def feedback(request: django.http.HttpRequest) -> django.http.HttpResponse:
    template = 'feedback/feedback.html'
    form = forms.FeedbackForm()

    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save(request.FILES.getlist('files'))

                send_mail(
                    'Feedback',
                    f'Thanks for the feedback <br> Your message '
                    f'- « {form.cleaned_data["text"]} »',
                    settings.MAIL_SENDER,
                    [f'{form.cleaned_data["email"]}'],
                    fail_silently=False,
                )

                messages.success(
                    request, 'Thank you for the confidential communication =)'
                )
            except:
                messages.success(
                    request, 'Write error =('
                )

            return django.shortcuts.redirect('feedback:feedback')

    context = {
        'form': form,
    }

    return django.shortcuts.render(request, template, context)
