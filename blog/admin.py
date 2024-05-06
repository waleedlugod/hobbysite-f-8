from django.contrib import admin

from .models import Article, ArticleCategory, Comment, ArticleImage


class ArticleInline(admin.TabularInline):
    model = Article


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline]


class CommentAdmin(admin.ModelAdmin):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [ArticleImageInline]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
