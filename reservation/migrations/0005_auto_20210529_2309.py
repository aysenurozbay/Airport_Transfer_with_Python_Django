# Generated by Django 3.1.7 on 2021-05-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20210529_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='time',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
