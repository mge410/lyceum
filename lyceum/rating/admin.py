from django.contrib import admin
import rating.models


@admin.register(rating.models.Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        rating.models.Grade.id.field.name,
        rating.models.Grade.rating.field.name,
        rating.models.Grade.user.field.name,
        rating.models.Grade.item.field.name,
        rating.models.Grade.created_at.field.name,
    )
    list_editable = (rating.models.Grade.rating.field.name,)
    list_display_links = (rating.models.Grade.id.field.name,)
