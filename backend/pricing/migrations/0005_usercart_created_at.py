# Generated by Django 3.2 on 2021-11-24 18:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0004_auto_20211124_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
