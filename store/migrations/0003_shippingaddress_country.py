# Generated by Django 4.0.3 on 2022-04-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=models.CharField(default='Chile', max_length=200),
        ),
    ]