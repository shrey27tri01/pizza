# Generated by Django 3.0.7 on 2020-06-21 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200621_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='items',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
