from django import forms
from .models import Comment, Article, ArticleImage


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "category", "entry", "header_image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "category", "entry", "header_image"]


class ArticleImagesForm(forms.Form):
    images = forms.FileField(
        widget=forms.TextInput(
            attrs={
                "name": "images",
                "type": "file",
                "class": "form-control",
                "multiple": "true",
            }
        ),
        label="Upload Images for Gallery",
    )
