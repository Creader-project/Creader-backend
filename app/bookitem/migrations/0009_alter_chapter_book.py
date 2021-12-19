# Generated by Django 3.2.7 on 2021-09-05 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookitem', '0008_auto_20210905_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='bookitem.book', verbose_name='book'),
        ),
    ]
