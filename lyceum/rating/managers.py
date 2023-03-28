import django.db.models


class GradeManager(django.db.models.Manager):
    def get_item_grades(self, item_id):
        return (
            self.get_queryset()
            .select_related(
                'item',
            )
            .filter(item__id=item_id)
            .only('rating', 'item__id', 'user__id')
        )
