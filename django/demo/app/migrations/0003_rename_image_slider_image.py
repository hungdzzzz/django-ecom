# Generated by Django 4.0.6 on 2022-07-27 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_banner_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='Image',
            new_name='image',
        ),
    ]
