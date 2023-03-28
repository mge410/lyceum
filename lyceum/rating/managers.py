import django.db.models
import rating.models
from django.contrib.auth.models import User


class GradeManager(django.db.models.Manager):
    def get_item_grades(self, item_id):
        return (
            self.get_queryset()
            .select_related(
                rating.models.Grade.item.field.name,
            )
            .select_related(
                rating.models.Grade.user.field.name,
            )
            .filter(item__id=item_id)
            .only(
                rating.models.Grade.rating.field.name,
                f'{rating.models.Grade.item.field.name}'
                f'__{User.id.field.name}',
                f'{rating.models.Grade.user.field.name}'
                f'__{User.id.field.name}',
            )
        )
