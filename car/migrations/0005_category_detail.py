# Generated by Django 3.1.7 on 2021-03-23 07:23

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20210321_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Models'),
        ),
    ]
