# Generated by Django 3.1.7 on 2021-06-13 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0017_auto_20210529_1809'),
        ('reservation', '0006_auto_20210529_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_id', models.IntegerField()),
                ('from_location_id', models.IntegerField()),
                ('to_location_id', models.IntegerField()),
                ('price', models.FloatField(default='0')),
                ('airline', models.CharField(max_length=50, null=True)),
                ('flightnumber', models.CharField(max_length=50, null=True)),
                ('flightarrivedate', models.CharField(max_length=50, null=True)),
                ('flightarrivetime', models.CharField(max_length=50, null=True)),
                ('pickuptime', models.CharField(max_length=50, null=True)),
                ('ip', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Waiting', 'Waiting'), ('Confirmed', 'Confirmed'), ('Canceled', 'Canceled')], default='New', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReserveCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Canceled', 'Canceled')], default='New', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('reserve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
