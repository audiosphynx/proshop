# Generated by Django 3.1.7 on 2021-03-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_shippingaddress_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]