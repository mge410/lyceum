from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from feedback.forms import FeedbackForm


def feedback(request: HttpRequest) -> HttpResponse:
    template = 'feedback/feedback.html'
    form = FeedbackForm(request.POST or None)

    if form.is_valid():
        send_mail(
            'Feedback',
            f'Thanks for the feedback <br> Your message '
            f'- « {form.cleaned_data["text"]} »',
            settings.MAIL_SENDER,
            [f'{form.cleaned_data["email"]}'],
            fail_silently=False,
        )
        return redirect('catalog:item_list')
    context = {'form': form}
    return render(request, template, context)
