# Generated by Django 2.2.5 on 2020-02-22 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_account_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Company description')),
                ('public_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('tags', models.TextField(blank=True, null=True, verbose_name='Tags')),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_seller', models.BooleanField(blank=True, null=True)),
                ('is_buyer', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='extension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserExtension'),
        ),
    ]
