# Generated by Django 3.1.5 on 2021-01-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=20, verbose_name='География'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='MEDIA_COMPANY_IMAGE_DIR', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название компании'),
        ),
    ]
