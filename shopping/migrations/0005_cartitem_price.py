# Generated by Django 3.2.5 on 2021-07-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_remove_cartitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(default=1),
        ),
    ]
