# Generated by Django 4.1.5 on 2023-02-17 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Order_id',
            new_name='order_id',
        ),
    ]
