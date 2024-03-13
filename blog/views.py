from django.shortcuts import render


def blog_list(request):
    ctx = {"message": "Hello World"}

    return render(request, "blog_list.html", ctx)


def blog_detail(request):
    ctx = {"message": "Hello World"}

    return render(request, "blog_detail.html", ctx)


# Create your views here.
