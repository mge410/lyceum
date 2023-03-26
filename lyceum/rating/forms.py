import rating.models
from django.forms import ModelForm


class GradeForm(ModelForm):
    class Meta:
        model = rating.models.Grade
        fields = [
            rating.models.Grade.rating.field.name,
        ]
