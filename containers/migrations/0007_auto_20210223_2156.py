# Generated by Django 3.1.6 on 2021-02-24 02:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0006_delete_steamship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z]{4}\\d{6}\\-\\d{1}')]),
        ),
    ]