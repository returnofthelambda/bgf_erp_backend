# Generated by Django 3.1.6 on 2021-02-23 19:10

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookings.booking')),
            ],
            bases=('bookings.booking',),
        ),
        migrations.CreateModel(
            name='Steamship',
            fields=[
                ('steamship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookings.steamship')),
            ],
            bases=('bookings.steamship',),
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=12)),
                ('pickup_date', models.DateField()),
                ('load_date', models.DateField(blank=True, null=True)),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('steamship', models.CharField(choices=[('CMA', 'CMA'), ('HMM', 'Hyundai'), ('MSC', 'MSC'), ('OOCL', 'OOCL'), ('ONE', 'ONE'), ('ZIM', 'ZIM')], max_length=20)),
                ('railyard', models.CharField(choices=[('NS', 'NorfolkSouthern'), ('CSX', 'CSX')], max_length=20)),
                ('size', models.CharField(choices=[('20', '20 foot'), ('40S', '40 foot standard'), ('40H', '40 foot highcube')], max_length=20)),
                ('status', models.CharField(blank=True, choices=[('PS', 'Pre-Shipment'), ('LG', 'Loading'), ('LD', 'Loaded'), ('DP', 'Departed'), ('SL', 'Sailed')], default='Pre-Shipment', max_length=10)),
                ('booking', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='steamship', chained_model_field='steamship', on_delete=django.db.models.deletion.CASCADE, to='bookings.booking')),
            ],
        ),
    ]
