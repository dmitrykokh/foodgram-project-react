# Generated by Django 2.2.20 on 2022-10-26 06:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221023_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальное время приготовления 1 минута')], verbose_name='время приготовления'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='text',
            field=models.TextField(verbose_name='Описание'),
            preserve_default=False,
        ),
    ]