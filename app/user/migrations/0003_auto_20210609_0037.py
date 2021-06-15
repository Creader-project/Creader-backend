# Generated by Django 3.2.4 on 2021-06-08 23:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210603_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='authuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(4, 'Admin'), (1, 'Reader'), (2, 'Author'), (3, 'Editor')], default=1, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('e0ae24fe-86dd-4b6c-95f2-1e15ae870b65'), editable=False, unique=True, verbose_name='Public identifier'),
        ),
    ]