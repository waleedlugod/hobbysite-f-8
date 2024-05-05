from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required

from .models import Article, ArticleCategory, Comment
from .forms import CommentForm


def blog_list_view(request):
    categories = ArticleCategory.objects.all()
    ctx = {
        "categories": categories,
        "register_url": reverse("user_management:register"),
    }

    return render(request, "blog/blog_list.html", ctx)


@login_required
def blog_detail_view(request, pk):
    comment_form = CommentForm()
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment()
            comment.author = request.user.profile
            comment.entry = comment_form.cleaned_data.get("entry")
            comment.article = article
            comment.save()
            comment_form = CommentForm()

    ctx = {
        "article": article,
        "comment_form": comment_form,
        "blog_list_url": reverse("blog:blog-list"),
    }

    return render(request, "blog/blog_detail.html", ctx)


# Create your views here.
