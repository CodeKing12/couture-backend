# Generated by Django 4.1.7 on 2023-03-17 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_product_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredient',
            new_name='Composition',
        ),
    ]
