# Generated by Django 5.0.7 on 2024-07-21 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('gasto', '0002_remove_gasto_items_gasto_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gastos', to='categories.category'),
        ),
    ]