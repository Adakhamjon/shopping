# Generated by Django 3.2.5 on 2021-08-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0012_coupon_coupon_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='is_used',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
