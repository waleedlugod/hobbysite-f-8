from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article, ArticleCategory


def blog_list_view(request):
    categories = ArticleCategory.objects.all()
    ctx = {"categories": categories}

    return render(request, "blog/blog_list.html", ctx)


@login_required
def blog_detail_view(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = {"article": article}

    return render(request, "blog/blog_detail.html", ctx)


# Create your views here.
