from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

import feedback.forms as forms


class FeedbackView(FormView):
    form_class = forms.FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = reverse_lazy('feedback:feedback')

    def form_valid(self, form: forms.FeedbackForm):
        try:
            form.save(self.request.FILES.getlist('files'))

            send_mail(
                'Feedback',
                f'Thanks for the feedback <br> Your message '
                f'- « {form.cleaned_data["text"]} »',
                settings.MAIL_SENDER,
                [f'{form.cleaned_data["email"]}'],
                fail_silently=False,
            )

            messages.success(
                self.request, 'Thank you for the confidential communication =)'
            )
        except Exception:
            messages.success(self.request, 'Write error =(')
        return super().form_valid(form)
