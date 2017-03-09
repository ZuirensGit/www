from django.contrib import admin
from .models import Post, Editor, Category, Menu, Page
from ghoster.admin import GhosterAdmin
from django.db import models


class PostAdmin(GhosterAdmin):
    title_field = 'title'
    markdown_field = 'content'
    list_display = ('short_title', 'editor', 'image_thumb', 'page', 'category', 'date', 'publish')
    list_editable = ('page', 'category', 'publish')
    list_filter = ('page__title', 'editor__name')
    # prepopulated_fields = {"slug": ("title",)}
    # search_fields = ('tags', 'editor__name',)
    # change_form_template = 'admin/ghoster_change_form.html'
    # add_form_template = 'admin/ghoster_change_form.html'

class EditorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Register your models here.



admin.site.register(Post, PostAdmin)
admin.site.register(Editor, EditorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
