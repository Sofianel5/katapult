# Generated by Django 2.2.5 on 2019-09-30 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Adspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('term_length', models.CharField(choices=[('2w', 'Two week'), ('1m', 'One month'), ('3m', 'Three months'), ('6m', 'Six months'), ('1y', 'One year'), ('2y', 'Two year'), ('3y', 'Three year')], max_length=2)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='adspace_pics')),
                ('description', models.TextField()),
                ('active', models.BooleanField()),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Address')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Buyer')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Seller')),
            ],
        ),
    ]
