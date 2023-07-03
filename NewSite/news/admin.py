from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    prepopulated_fields = {"slug": ('title',)}
    fields = ('title', 'slug', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')


    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    prepopulated_fields = {"slug": ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'content', 'get_html_photo')
    list_display_links = ('id', 'title')
    search_fields = ('time_create',)
    fields = ('title', 'email', 'content', 'photo', 'get_html_photo', 'time_create')
    readonly_fields = ('time_create', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}




admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Message, MessageAdmin)


admin.site.site_title = 'Админ-панель игры'
admin.site.site_header = 'Админ-панель игры'

