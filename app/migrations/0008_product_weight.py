# Generated by Django 4.2 on 2023-05-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_filament_hex'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.FloatField(default=200),
            preserve_default=False,
        ),
    ]