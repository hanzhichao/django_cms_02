# coding=utf-8
from django.contrib import admin
from cms.models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created', 'modified')
    search_fields = ('title', 'content')
    list_filter = ('status', 'author', 'category', 'created', 'modified')
    # prepopulated_fields = {'slug': ('title',)}  # 同步slug与title相同


class CategoryAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {'slug': ('label',)}  # 同步slug与title相同

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
