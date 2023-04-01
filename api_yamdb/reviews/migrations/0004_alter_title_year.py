# Generated by Django 3.2 on 2023-04-01 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_title_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2023)], verbose_name='Publication year'),
        ),
    ]
