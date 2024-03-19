from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article, ArticleCategory


def blog_list_view(request):
    categories = ArticleCategory.objects.all()
    articles = Article.objects.all()
    ctx = {"categories": categories, "articles": articles}

    return render(request, "blog_list.html", ctx)


def blog_detail_view(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = {"article": article}

    return render(request, "blog_detail.html", ctx)


# Create your views here.
