# Generated by Django 5.0.2 on 2024-02-28 22:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_image', models.ImageField(upload_to='core_images')),
            ],
        ),
        migrations.CreateModel(
            name='Product_variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_variant_sku', models.CharField(max_length=100, unique=True)),
                ('product_variant_name', models.CharField(max_length=255)),
                ('product_variant_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_variant_details', models.TextField()),
                ('product_variant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
    ]
