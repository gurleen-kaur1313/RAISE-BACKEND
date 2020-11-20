# Generated by Django 3.1.1 on 2020-11-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthEmergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('problem', models.TextField(help_text='Problem : ')),
                ('longitude', models.IntegerField()),
                ('latitude', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HealthTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(blank=True, choices=[('covid_symptoms', 'Covid-19 Symptoms')], max_length=250, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('remarksDoc', models.CharField(blank=True, max_length=255, null=True)),
                ('remarksPat', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PoliceEmergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('longitude', models.IntegerField()),
                ('latitude', models.IntegerField()),
            ],
        ),
    ]