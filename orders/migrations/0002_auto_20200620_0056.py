# Generated by Django 3.0.7 on 2020-06-19 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dinnerplatters',
            options={'verbose_name_plural': 'DinnerPlatters'},
        ),
        migrations.AlterModelOptions(
            name='pasta',
            options={'verbose_name_plural': 'Pasta'},
        ),
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name_plural': 'Pizzas'},
        ),
        migrations.AlterModelOptions(
            name='salads',
            options={'verbose_name_plural': 'Salads'},
        ),
        migrations.AlterModelOptions(
            name='subs',
            options={'verbose_name_plural': 'Subs'},
        ),
        migrations.AlterModelOptions(
            name='toppings',
            options={'verbose_name_plural': 'Toppings'},
        ),
        migrations.RemoveField(
            model_name='dinnerplatters',
            name='id',
        ),
        migrations.RemoveField(
            model_name='dinnerplatters',
            name='price',
        ),
        migrations.RemoveField(
            model_name='pasta',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pasta',
            name='price',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='price',
        ),
        migrations.RemoveField(
            model_name='salads',
            name='id',
        ),
        migrations.RemoveField(
            model_name='salads',
            name='price',
        ),
        migrations.RemoveField(
            model_name='subs',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subs',
            name='price',
        ),
        migrations.AddField(
            model_name='dinnerplatters',
            name='product_ptr',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Product'),
        ),
        migrations.AddField(
            model_name='pasta',
            name='product_ptr',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Product'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='product_ptr',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Product'),
        ),
        migrations.AddField(
            model_name='salads',
            name='product_ptr',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Product'),
        ),
        migrations.AddField(
            model_name='subs',
            name='product_ptr',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Product'),
        ),
    ]
