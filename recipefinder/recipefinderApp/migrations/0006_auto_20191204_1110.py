# Generated by Django 2.2.7 on 2019-12-04 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipefinderApp', '0005_preferences_cooking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='cooking_time',
            field=models.CharField(max_length=50),
        ),
    ]