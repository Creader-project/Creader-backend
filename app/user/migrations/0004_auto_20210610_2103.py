# Generated by Django 3.2.4 on 2021-06-10 20:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210609_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(4, 'Admin'), (2, 'Author'), (3, 'Editor'), (1, 'Reader')], default=1, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('8fb58fd0-0d56-4518-9eb5-fa8d98a33ffd'), editable=False, unique=True, verbose_name='Public identifier'),
        ),
    ]