from feedback.models import FeedbackFiles
from feedback.models import Feedback
from feedback.models import FeedbackDataUser
from django.contrib import admin


class FeedbackDataUserAdmin(admin.TabularInline):
    model = FeedbackDataUser
    extra = 1

    readonly_fields = (model.email.field.name,)


class FeedbackFilesAdmin(admin.TabularInline):
    model = FeedbackFiles
    extra = 1


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        Feedback.id.field.name,
    )
    inlines = [FeedbackDataUserAdmin, FeedbackFilesAdmin]