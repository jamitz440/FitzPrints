# Generated by Django 4.2 on 2023-04-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='filament_used',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='print_time',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='source_link',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
