# Generated by Django 3.1.7 on 2021-03-31 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_auto_20210329_2334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='car.category'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'parent')},
        ),
    ]
