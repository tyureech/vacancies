# Generated by Django 3.1.5 on 2021-01-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='login',
            field=models.CharField(max_length=20),
        ),
    ]