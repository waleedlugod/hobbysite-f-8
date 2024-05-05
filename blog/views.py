from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required

from .models import Article, ArticleCategory, Comment
from .forms import CommentForm, UpdateForm


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
        "update_url": reverse("blog:blog-update", args=[pk]),
    }

    return render(request, "blog/blog_detail.html", ctx)


@login_required
def blog_create_view(request):
    ctx = {}
    return render(request, "blog/blog_create.html", ctx)


@login_required
def blog_update_view(request, pk):
    update_form = UpdateForm()
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        update_form = UpdateForm(request.POST, request.FILES)
        if update_form.is_valid():
            article.title = update_form.cleaned_data.get("title")
            article.category = update_form.cleaned_data.get("category")
            article.entry = update_form.cleaned_data.get("entry")
            article.header_image = update_form.cleaned_data.get("header_image")
            article.save()

            return redirect("blog:blog-detail", pk=pk)
    ctx = {"update_form": update_form, "article": article}
    return render(request, "blog/blog_update.html", ctx)
