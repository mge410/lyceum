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
            .filter(item__id=item_id)
            .only(
                rating.models.Grade.rating.field.name,
                f'{rating.models.Grade.item.field.name}'
                f'__{User.id.field.name}',
                f'{rating.models.Grade.user.field.name}'
                f'__{User.id.field.name}',
            )
        )

    def get_filtered_items(self, user_id):
        return (
            rating.models.Grade.objects.filter(user_id=user_id)
            .select_related(rating.models.Grade.item.field.name)
            .order_by(rating.models.Grade.rating.field.name)
        )
