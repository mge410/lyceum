import django.forms
from django.forms import ModelForm

import rating.models


class GradeForm(ModelForm):
    class Meta:
        model = rating.models.Grade
        fields = ('rating',)
        widgets = {
            'rating': django.forms.widgets.Select(
                attrs={'class': 'form-select'}
            )
        }
