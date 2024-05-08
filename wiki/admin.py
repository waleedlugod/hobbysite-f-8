from django.contrib import admin
from .models import ArticleCategory, Article, Comment, ArticleImage


class ArticleInline(admin.TabularInline):
    model = Article


class CommentAdmin(admin.ModelAdmin):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline]


class ArticleImageAdmin(admin.ModelAdmin):
    model = ArticleImage


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleImage, ArticleImageAdmin)

# Register your models here.
