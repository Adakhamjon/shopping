# Generated by Django 3.2.5 on 2021-07-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_auto_20210720_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=254, null=True),
        ),
    ]