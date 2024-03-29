# Generated by Django 3.2.10 on 2021-12-30 21:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Reader'), (2, 'Author'), (4, 'Admin'), (3, 'Editor')], default=1, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('31c604d4-af97-4d83-9ed0-9fccd7663cd8'), editable=False, unique=True, verbose_name='Public identifier'),
        ),
    ]
