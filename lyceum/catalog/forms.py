from django.forms import ModelForm
import rating.models
from django.utils.translation import gettext as _


class GradeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = rating.models.Grade
        fields = [
            rating.models.Grade.rating.field.name,
        ]
        labels = {rating.models.Grade.rating.field.name: _("Your rating")}
        help_texts = {
            rating.models.Grade.rating.field.name: _("Add your rating")
        }
