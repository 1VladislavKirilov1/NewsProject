from django.contrib import admin
from .models import Category, Post
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(TranslationAdmin):
    model = Category


class TextAdmin(TranslationAdmin):
    model = Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author',)
    list_filter = ('author',)
    search_fields = ('author', 'postCategory',)


admin.site.register(Category, TextAdmin)
admin.site.register(Post, PostAdmin)