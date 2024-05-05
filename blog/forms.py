from django import forms
from .models import Comment, Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "category", "entry", "header_image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry"]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "category", "entry", "header_image"]
