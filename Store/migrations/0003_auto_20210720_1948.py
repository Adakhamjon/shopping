# Generated by Django 3.2.5 on 2021-07-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_auto_20210720_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
