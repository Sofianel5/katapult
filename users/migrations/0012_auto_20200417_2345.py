# Generated by Django 3.0.4 on 2020-04-17 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200222_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adspace',
            name='image',
            field=models.ImageField(default='adspace_pics/default.jpg', upload_to='adspace_pics'),
        ),
    ]
