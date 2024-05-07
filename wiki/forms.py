from django import forms
from .models import Article, Comment


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "entry", "category", "header_image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry"]
