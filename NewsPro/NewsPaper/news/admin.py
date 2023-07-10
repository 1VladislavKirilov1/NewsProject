from django.contrib import admin
from .models import Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author',)
    list_filter = ('author',)
    search_fields = ('author', 'postCategory',)

admin.site.register(Category)
admin.site.register(Post, PostAdmin)