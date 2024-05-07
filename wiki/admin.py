from django.contrib import admin
from .models import ArticleCategory, Article, Comment


class ArticleInline(admin.TabularInline):
    model = Article


class CommentAdmin(admin.ModelAdmin):
    model = Comment


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Comment, CommentAdmin)

# Register your models here.
