# Generated by Django 4.0.6 on 2022-09-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_cart_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_total',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
