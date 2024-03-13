from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article, ArticleCategory


class BlogListView(ListView):
    model = ArticleCategory
    template_name = "blog_list.html"


class BlogDetailView(DetailView):
    model = Article
    template_nmae = "blog_detail.html"


# Create your views here.
