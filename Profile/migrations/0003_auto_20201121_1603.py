# Generated by Django 3.1.1 on 2020-11-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20201121_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.TextField(blank=True, help_text='City : ', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.TextField(blank=True, help_text='State : ', null=True),
        ),
    ]
