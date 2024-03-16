from django.shortcuts import render
from .models import Article


def article_list_view(request):
    articles = Article.objects.all()
    ctx = {"articles": articles}
    return render(request, "article_list_view.html", ctx)


def article_detail_view(request):
    ctx = {"article", Article.objects.get(id=id)}
    return render(request, "article_detail_view.html", ctx)


# Create your views here.
