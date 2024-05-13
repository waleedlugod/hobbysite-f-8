# Generated by Django 5.0.2 on 2024-05-11 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_articles', to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_articles', to='blog.articlecategory'),
        ),
        migrations.AddField(
            model_name='articleimage',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.article'),
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='blog.article'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_comments', to='user_management.profile'),
        ),
    ]
