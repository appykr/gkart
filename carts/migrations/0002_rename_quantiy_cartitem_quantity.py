# Generated by Django 5.1.4 on 2024-12-17 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quantiy',
            new_name='quantity',
        ),
    ]