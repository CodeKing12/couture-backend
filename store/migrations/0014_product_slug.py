# Generated by Django 4.1.7 on 2023-03-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(auto_created=True, default='default', max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
