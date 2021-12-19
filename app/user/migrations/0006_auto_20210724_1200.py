# Generated by Django 3.2.4 on 2021-07-24 11:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210723_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(3, 'Editor'), (1, 'Reader'), (2, 'Author'), (4, 'Admin')], default=1, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('1b2f7487-7f93-4505-8e51-ebd498fe3b3d'), editable=False, unique=True, verbose_name='Public identifier'),
        ),
    ]
