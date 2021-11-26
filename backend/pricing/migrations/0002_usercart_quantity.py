# Generated by Django 3.2 on 2021-11-19 04:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)]),
        ),
    ]