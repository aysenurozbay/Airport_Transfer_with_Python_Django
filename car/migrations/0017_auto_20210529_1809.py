# Generated by Django 3.1.7 on 2021-05-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0016_auto_20210522_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='base_price',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='car',
            name='capasity',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='km_price',
            field=models.FloatField(default='0'),
        ),
    ]