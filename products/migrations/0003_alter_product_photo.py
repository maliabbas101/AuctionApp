# Generated by Django 4.1.5 on 2023-01-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='media/prod_c8m26c.png', upload_to='media/products/'),
        ),
    ]
