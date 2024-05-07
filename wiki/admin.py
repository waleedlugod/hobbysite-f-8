from django.contrib import admin
from .models import ArticleCategory, Article, Comment


class ArticleInline(admin.TabularInline):
    model = Article


class CommentAdmin(admin.ModelAdmin):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)

# Register your models here.
