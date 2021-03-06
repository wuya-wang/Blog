# Generated by Django 3.1.7 on 2021-03-20 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='relation',
            new_name='article_tag',
        ),
        migrations.RemoveField(
            model_name='category',
            name='relation',
        ),
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article_category', to='blog.category'),
        ),
    ]
