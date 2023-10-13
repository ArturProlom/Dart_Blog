from django.contrib import admin
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe


# Register your models here.

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
    form = PostAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('views', 'created_at', 'get_photo')
    list_filter = ('category', 'tags')
    fields = ('title', 'slug', 'category', 'author', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75"')
        else:
            return '-'

    get_photo.short_description = 'Photo-mini'


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title',)
    search_fields = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
