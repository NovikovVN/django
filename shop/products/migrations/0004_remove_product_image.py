# Generated by Django 2.1.1 on 2018-10-14 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
