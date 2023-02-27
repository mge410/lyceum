from catalog.models import Category, Item, Tag, MainImageItem
from django.contrib import admin


@admin.register(MainImageItem)
class MainImageItemAdmin(admin.ModelAdmin):
    list_display = (
        MainImageItem.image_tmb,
    )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        Item.name.field.name,
        Item.is_published.field.name,
        Item.main_image.field.name,
    )
    list_editable = (Item.is_published.field.name,)
    list_display_links = (Item.name.field.name,)
    filter_horizontal = (Item.tags.field.name,)
    fields = (
        Item.is_published.field.name,
        Item.name.field.name,
        Item.main_image.field.name,
        Item.category.field.name,
        Item.tags.field.name,
        Item.text.field.name,
    )


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
