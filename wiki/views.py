from django.shortcuts import render
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    ctx = {"articles": articles}
    return render(request, "list_view.html", ctx)


def article_detail(request):
    ctx = {"article", Article.objects.get(id=id)}
    return render(request, "detail_view.html", ctx)


# Create your views here.
