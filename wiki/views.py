from django.shortcuts import render
from .models import Article, ArticleCategory


def article_list_view(request):
    articles = Article.objects.all()
    category = Article.Category.all()
    ctx = {"articles": articles, "category": category}
    return render(request, "article_list_view.html", ctx)


def article_detail_view(request, pk):
    ctx = {"article", Article.objects.get(pk=pk)}
    return render(request, "article_detail_view.html", ctx)


# Create your views here.
