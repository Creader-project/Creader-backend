# Generated by Django 3.2.4 on 2021-08-10 00:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bookitem', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='love',
        ),
    ]
