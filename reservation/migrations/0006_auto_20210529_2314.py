# Generated by Django 3.1.7 on 2021-05-29 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_auto_20210529_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopcart',
            old_name='fromlocation',
            new_name='from_location',
        ),
        migrations.RenameField(
            model_name='shopcart',
            old_name='tolocation',
            new_name='to_location',
        ),
    ]
