# Generated by Django 3.2.5 on 2021-08-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_coupon_is_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(blank=True, max_length=8, unique=True),
        ),
    ]
