from typing import Any

from catalog.models import Category
from catalog.models import GalleryImagesItem
from catalog.models import Item
from catalog.models import MainImageItem
from catalog.models import Tag
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin


class ItemTextAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Item
        fields = '__all__'


class MainImageAdmin(admin.TabularInline):
    model = MainImageItem
    extra = 1

    readonly_fields = (model.image_tmb,)


class GalleryImageAdmin(admin.TabularInline):
    model = GalleryImagesItem
    extra = 1

    readonly_fields = (model.image_tmb,)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        Item.name.field.name,
        Item.is_published.field.name,
        Item.is_on_main.field.name,
        'get_image',
    )
    form = ItemTextAdminForm
    inlines = [MainImageAdmin, GalleryImageAdmin]
    list_editable = (
        Item.is_published.field.name,
        Item.is_on_main.field.name,
    )
    list_display_links = (Item.name.field.name,)
    filter_horizontal = (Item.tags.field.name,)
    fields = (
        Item.is_published.field.name,
        Item.is_on_main.field.name,
        Item.name.field.name,
        Item.category.field.name,
        Item.tags.field.name,
        Item.text.field.name,
    )

    @admin.display(ordering='main_image', description='Фото товара')
    def get_image(self, obj: Any) -> str:
        return obj.main_image.image_tmb()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        Category.name.field.name,
        Category.is_published.field.name,
        Category.slug.field.name,
        Category.weight.field.name,
    )
    list_editable = (
        Category.is_published.field.name,
        Category.slug.field.name,
        Category.weight.field.name,
    )
    list_display_links = (Category.name.field.name,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        Tag.name.field.name,
        Tag.is_published.field.name,
        Tag.slug.field.name,
    )
    list_editable = (
        Tag.is_published.field.name,
        Tag.slug.field.name,
    )
    list_display_links = (Tag.name.field.name,)
