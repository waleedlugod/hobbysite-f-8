from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article, ArticleCategory, Comment, ArticleImage
from .forms import ArticleCreateForm, CommentForm, ArticleImagesForm


def article_list_view(request):
    category = ArticleCategory.objects.all()
    article = Article.objects.all()
    ctx = {"categories": category, "articles": article}
    return render(request, "wiki/article_list_view.html", ctx)


def article_detail_view(request, pk):
    category = ArticleCategory.objects.all()
    all_articles = Article.objects.all()
    comments = Comment.objects.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.author = request.user.profile
            comment.article = Article.objects.get(pk=pk)
            comment.entry = form.cleaned_data.get("entry")
            comment.save()
    ctx = {
        "this_article": Article.objects.get(pk=pk),
        "categories": category,
        "all_articles": all_articles,
        "comments": comments,
        "form": form,
    }
    return render(request, "wiki/article_detail_view.html", ctx)


@login_required
def article_update_view(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleCreateForm()

    if request.method == "POST":
        image_form = ArticleImagesForm(request.POST, request.FILES)
        form = ArticleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            article.title = form.cleaned_data.get("title")
            article.entry = form.cleaned_data.get("entry")
            article.category = form.cleaned_data.get("category")
            article.header_image = form.cleaned_data.get("header_image")
            article.save()

    ctx = {"form": form}
    return render(request, "wiki/article_update_view.html", ctx)


@login_required
def article_create_view(request):
    form = ArticleCreateForm()
    image_form = ArticleImagesForm()

    if request.method == "POST":
        image_form = ArticleImagesForm(request.POST, request.FILES)
        form = ArticleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            article = Article()
            article.author = request.user.profile
            article.title = form.cleaned_data.get("title")
            article.entry = form.cleaned_data.get("entry")
            article.category = form.cleaned_data.get("category")
            article.header_image = form.cleaned_data.get("header_image")
            article.save()

        images = request.FILES.getlist("images")
        for image in images:
            imageobj = ArticleImage()
            imageobj.article = article
            imageobj.image = image
            imageobj.save()
    ctx = {"form": form, "image_form": image_form}
    return render(request, "wiki/article_create_view.html", ctx)


@login_required
def article_upload_image_view(request, pk):
    images_form = ArticleImagesForm()
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        images_form = ArticleImagesForm(request.POST, request.FILES)
        images = request.FILES.getlist("images")
        for image in images:
            imageobj = ArticleImage()
            imageobj.article = article
            imageobj.image = image
            imageobj.save()
    ctx = {
        "images_form": images_form,
        "article": article,
    }

    return render(request, "wiki/article_upload_image_view.html", ctx)


# Create your views here.
