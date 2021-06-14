# Generated by Django 3.1.7 on 2021-05-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20210529_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcart',
            name='distance',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='fromlocation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='tolocation',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
