# Generated by Django 4.0.6 on 2022-08-07 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_product_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='app_Product',
        ),
    ]