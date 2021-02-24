# Generated by Django 3.1.6 on 2021-02-23 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
        ('containers', '0004_auto_20210223_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='steamship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.steamship'),
        ),
    ]