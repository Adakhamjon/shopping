# Generated by Django 3.2.5 on 2021-07-27 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='price',
        ),
    ]
