# Generated by Django 2.1.11 on 2020-01-09 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user_id',
            new_name='user',
        ),
    ]