# Generated by Django 4.2 on 2023-05-01 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_productfilament'),
    ]

    operations = [
        migrations.AddField(
            model_name='filament',
            name='hex',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
