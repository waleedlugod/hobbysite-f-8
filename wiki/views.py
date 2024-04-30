from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article, ArticleCategory


def article_list_view(request):
    category = ArticleCategory.objects.all()
    ctx = {"categories": category}
    return render(request, "wiki_templates/article_list_view.html", ctx)


@login_required
def article_detail_view(request, pk):
    ctx = {"article": Article.objects.get(pk=pk)}
    return render(request, "wiki_templates/article_detail_view.html", ctx)


# Create your views here.
