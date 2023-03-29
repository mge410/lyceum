import django.forms
from django.forms import ModelForm
from django.utils.translation import gettext as _
import rating.models

import rating.models


class GradeForm(ModelForm):
    delete_grade = django.forms.BooleanField(initial=False, required=False)

    def __init__(self, *args, **kwargs) -> None:
        super(GradeForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = rating.models.Grade
        fields = [
            rating.models.Grade.rating.field.name,
            'delete_grade',
        ]
        labels = {
            rating.models.Grade.rating.field.name: _('Your rating'),
            'delete_grade': _('Delete grade'),
        }
        help_texts = {
            rating.models.Grade.rating.field.name: _('Add your rating'),
            'delete_grade': _('Delete grade'),
        }
