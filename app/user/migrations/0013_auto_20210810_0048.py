# Generated by Django 3.2.4 on 2021-08-09 23:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0012_auto_20210810_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True,
                                                   choices=[(1, 'Reader'), (4, 'Admin'), (2, 'Author'), (3, 'Editor')],
                                                   default=1, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('c254e0c9-eaf8-455d-9288-cbbd4dadcbfd'), editable=False,
                                   unique=True, verbose_name='Public identifier'),
        ),
    ]
