# Generated by Django 3.2.4 on 2021-07-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('payment', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(
                choices=[('ordered', 'Ordered'), ('completed', 'completed'), ('cancelled', 'Cancelled'),
                         ('refunded', 'Refunded')], default='ordered', max_length=20),
        ),
    ]
