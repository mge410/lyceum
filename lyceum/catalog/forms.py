from django.forms import ModelForm
import rating.models


class GradeForm(ModelForm):
    class Meta:
        model = rating.models.Grade
        fields = [rating.models.Grade.rating.field.name, ]
