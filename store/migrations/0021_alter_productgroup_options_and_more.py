# Generated by Django 4.1.7 on 2023-03-17 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_productgroup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productgroup',
            options={'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]
