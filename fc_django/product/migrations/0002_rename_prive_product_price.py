# Generated by Django 3.2.5 on 2021-07-05 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prive',
            new_name='price',
        ),
    ]