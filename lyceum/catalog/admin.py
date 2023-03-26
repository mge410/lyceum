from typing import Any

import catalog.models
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin


class ItemTextAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = catalog.models.Item
        fields = '__all__'


class MainImageAdmin(admin.TabularInline):
    model = catalog.models.MainImageItem
    extra = 1

    readonly_fields = (model.image_tmb,)


class GalleryImageAdmin(admin.TabularInline):
    model = catalog.models.GalleryImagesItem
    extra = 1

    readonly_fields = (model.image_tmb,)


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.is_on_main.field.name,
        'get_image',
    )
    form = ItemTextAdminForm
    inlines = [MainImageAdmin, GalleryImageAdmin]
    list_editable = (
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.is_on_main.field.name,
    )
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)
    fields = (
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.is_on_main.field.name,
        catalog.models.Item.name.field.name,
        catalog.models.Item.category.field.name,
        catalog.models.Item.tags.field.name,
        catalog.models.Item.text.field.name,
    )

    @admin.display(ordering='main_image', description='Фото товара')
    def get_image(self, obj: Any) -> str:
        return obj.main_image.image_tmb()


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
        catalog.models.Tag.slug.field.name,
    )
    list_editable = (
        catalog.models.Tag.is_published.field.name,
        catalog.models.Tag.slug.field.name,
    )
    list_display_links = (catalog.models.Tag.name.field.name,)
