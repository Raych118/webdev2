# Generated by Django 2.2 on 2020-07-08 09:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('email', models.EmailField(max_length=254)),
                ('question', models.TextField()),
                ('reply', models.TextField(default=None, null=True)),
                ('replied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pull',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
            ],
        ),
    ]