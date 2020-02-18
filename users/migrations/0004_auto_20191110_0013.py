# Generated by Django 2.2.5 on 2019-11-10 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191001_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemographicProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AgePercentUnder5', models.FloatField()),
                ('AgePercent5To9', models.FloatField()),
                ('AgePercent10To14', models.FloatField()),
                ('AgePercent15To19', models.FloatField()),
                ('AgePercent20To24', models.FloatField()),
                ('AgePercent25To34', models.FloatField()),
                ('AgePercent35To44', models.FloatField()),
                ('AgePercent45To54', models.FloatField()),
                ('AgePercent55To59', models.FloatField()),
                ('AgePercent60To64', models.FloatField()),
                ('Percent65To74', models.FloatField()),
                ('Percent75To84', models.FloatField()),
                ('Percent85AndOver', models.FloatField()),
                ('IncomePercentUnder10000', models.FloatField()),
                ('IncomePercent10000To14999', models.FloatField()),
                ('IncomePercent15000To24999', models.FloatField()),
                ('IncomePercent25000To34999', models.FloatField()),
                ('IncomePercent35000To49999', models.FloatField()),
                ('IncomePercent50000To74999', models.FloatField()),
                ('IncomePercent75000To99999', models.FloatField()),
                ('IncomePercent100000To149999', models.FloatField()),
                ('IncomePercent150000To199999', models.FloatField()),
                ('IncomePercent200000OrMore', models.FloatField()),
                ('PercentWhite', models.FloatField()),
                ('PercentBlack', models.FloatField()),
                ('PercentAmericanIndian', models.FloatField()),
                ('PercentAsian', models.FloatField()),
                ('PercentPacificIslander', models.FloatField()),
                ('PercentOtherRace', models.FloatField()),
                ('PercentHispanicOrLatinoOfAnyRace', models.FloatField()),
                ('PercentNotHispanicOrLatino', models.FloatField()),
                ('PercentMale', models.FloatField()),
                ('PercentFemale', models.FloatField()),
                ('PercentGradDegree', models.FloatField()),
                ('BachDegree', models.FloatField()),
                ('GradDegree', models.FloatField()),
                ('AssocDegree', models.FloatField()),
                ('SomeCollege', models.FloatField()),
                ('HighSchool', models.FloatField()),
                ('BelowHighSchool', models.FloatField()),
                ('EmployedWhiteCollar', models.FloatField()),
                ('Unemployed', models.FloatField()),
                ('BlueCollar', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='adspace',
            name='demographics',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.DemographicProfile'),
        ),
    ]