# Generated by Django 2.2.5 on 2020-02-22 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200222_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_buyer',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_seller',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
