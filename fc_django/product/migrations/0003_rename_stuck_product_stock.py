# Generated by Django 3.2.5 on 2021-07-06 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_prive_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stuck',
            new_name='stock',
        ),
    ]
