# Generated by Django 5.0.1 on 2024-04-20 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_wishlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
