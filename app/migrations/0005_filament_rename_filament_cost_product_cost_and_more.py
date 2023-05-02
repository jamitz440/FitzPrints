# Generated by Django 4.2 on 2023-05-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product_user_alter_product_profit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('material', models.CharField(choices=[('PLA', 'PLA'), ('ABS', 'ABS'), ('PETG', 'PETG'), ('TPU', 'TPU'), ('Nylon', 'Nylon'), ('ASA', 'ASA'), ('PC', 'PC'), ('Carbon Fibre', 'Carbon Fibre')], max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='filament_cost',
            new_name='cost',
        ),
        migrations.RemoveField(
            model_name='product',
            name='filament_used',
        ),
        migrations.AddField(
            model_name='product',
            name='filament_used',
            field=models.ManyToManyField(blank=True, to='app.filament'),
        ),
    ]