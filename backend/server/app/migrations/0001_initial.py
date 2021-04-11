# Generated by Django 3.1.7 on 2021-04-11 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('fuel', models.CharField(max_length=20)),
                ('unit', models.CharField(max_length=20)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meters', to='app.building')),
            ],
        ),
        migrations.CreateModel(
            name='EnergyConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.FloatField(max_length=15)),
                ('reading_date_time', models.DateTimeField(blank=True)),
                ('meter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='energy_consumptions', to='app.meter')),
            ],
        ),
    ]
