# Generated by Django 3.2.5 on 2021-08-21 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0008_auto_20210819_1856'),
        ('shopping', '0011_auto_20210819_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('stock', models.FloatField()),
                ('expires_in', models.DateTimeField()),
                ('category', models.ManyToManyField(to='Store.Subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=8)),
                ('stock', models.FloatField()),
                ('expires_in', models.DateTimeField()),
                ('category', models.ManyToManyField(to='Store.Subcategory')),
            ],
        ),
    ]