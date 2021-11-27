# Generated by Django 3.2 on 2021-11-27 04:48

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('gender', models.CharField(choices=[('', 'Select a Gender'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=3)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(message='Only alphabet is allowed', regex='^[a-zA-Z]*$')], verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(message='Only alphabet is allowed', regex='^[a-zA-Z]*$')], verbose_name='last name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
