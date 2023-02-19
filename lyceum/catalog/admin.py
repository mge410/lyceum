from catalog import models
from django.contrib import admin


@admin.register(models.Item)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        models.Item.name.field.name,
        models.Item.is_published.field.name,
    )
    list_editable = (models.Item.is_published.field.name,)
    list_display_links = (models.Item.name.field.name,)
    filter_horizontal = (models.Item.tags.field.name,)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        models.Category.name.field.name,
        models.Category.is_published.field.name,
        models.Category.slug.field.name,
        models.Category.weight.field.name,
    )
    list_editable = (
        models.Category.is_published.field.name,
        models.Category.slug.field.name,
        models.Category.weight.field.name,
    )
    list_display_links = (models.Category.name.field.name,)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        models.Tag.name.field.name,
        models.Tag.is_published.field.name,
        models.Tag.slug.field.name,
    )
    list_editable = (
        models.Tag.is_published.field.name,
        models.Tag.slug.field.name,
    )
    list_display_links = (models.Tag.name.field.name,)
