# Generated by Django 2.2.5 on 2019-11-10 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_campaign_marketsegment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Buyer'),
        ),
    ]
