# Generated by Django 3.2.4 on 2021-08-12 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookitem', '0006_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_commnet',
                                           to='bookitem.book')),
                ('dislikes',
                 models.ManyToManyField(blank=True, related_name='comment_dislikes', to=settings.AUTH_USER_MODEL)),
                (
                'likes', models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL)),
                ('parent',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies',
                                   to='comment.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': 'Comment',
                'ordering': ['-created_on'],
            },
        ),
    ]
