# Generated by Django 5.0.2 on 2024-05-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]