from django.contrib import admin

from feedback.models import Feedback, FeedbackFiles, FeedbackUserData


class FeedbackDataUserAdmin(admin.TabularInline):
    model = FeedbackUserData
    extra = 1

    readonly_fields = (model.email.field.name,)


class FeedbackFilesAdmin(admin.TabularInline):
    model = FeedbackFiles
    extra = 1


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (Feedback.id.field.name,)
    inlines = [FeedbackDataUserAdmin, FeedbackFilesAdmin]
