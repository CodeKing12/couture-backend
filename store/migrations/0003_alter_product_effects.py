# Generated by Django 4.1.7 on 2023-03-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_addons_remove_product_weights_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='effects',
            field=models.CharField(max_length=100),
        ),
    ]