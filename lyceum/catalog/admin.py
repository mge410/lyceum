import catalog.models
from django.contrib import admin


@admin.register(catalog.models.Item)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Category.name.field.name,
        catalog.models.Category.is_published.field.name,
        catalog.models.Category.slug.field.name,
        catalog.models.Category.weight.field.name,
    )
    list_editable = (
        catalog.models.Category.is_published.field.name,
        catalog.models.Category.slug.field.name,
        catalog.models.Category.weight.field.name,
    )
    list_display_links = (catalog.models.Category.name.field.name,)


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Tag.name.field.name,
        catalog.models.Tag.is_published.field.name,
        catalog.models.Category.slug.field.name,
    )
    list_editable = (
        catalog.models.Tag.is_published.field.name,
        catalog.models.Category.slug.field.name,
    )
    list_display_links = (catalog.models.Tag.name.field.name,)
