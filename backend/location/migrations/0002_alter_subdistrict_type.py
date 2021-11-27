# Generated by Django 3.2 on 2021-11-27 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdistrict',
            name='type',
            field=models.CharField(choices=[('Metro Cities', 'Metro Cities'), ('Sub-Metro Cities', 'Sub-Metro Cities'), ('Urban Municipalities', 'Municipalities'), ('Rural Municipalities', 'Rural Municipalities')], max_length=25),
        ),
    ]
