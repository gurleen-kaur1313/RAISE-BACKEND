# Generated by Django 3.1.1 on 2020-11-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmergencyServices', '0002_auto_20201121_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
