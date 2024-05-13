# Generated by Django 5.0.2 on 2024-05-11 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Article categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('entry', models.TextField()),
                ('header_image', models.ImageField(default='default.jpg', upload_to='images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='user_management.profile')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='wiki.articlecategory')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='wiki.article')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='wiki.article')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='user_management.profile')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
