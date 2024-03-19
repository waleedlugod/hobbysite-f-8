from django.contrib import admin
from .models import ArticleCategory, Article


class ArticleInline(admin.TabularInline):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)


# Register your models here.
