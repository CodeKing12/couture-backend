# Generated by Django 4.1.7 on 2023-03-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_slug_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(auto_created=True, max_length=250, unique=True),
        ),
    ]