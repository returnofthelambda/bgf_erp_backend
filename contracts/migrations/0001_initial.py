# Generated by Django 3.1.6 on 2021-02-23 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=50)),
                ('variety', models.CharField(max_length=20)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=15)),
                ('units', models.CharField(choices=[('MT', 'MT'), ('BU', 'BU'), ('LBS', 'LBS'), ('ST', 'ST')], max_length=10)),
                ('pkg', models.CharField(choices=[('BULK', 'BULK'), ('30KG', '30KG'), ('60#', '60#')], max_length=10)),
            ],
        ),
    ]
