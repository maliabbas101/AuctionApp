# Generated by Django 4.1.5 on 2023-01-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.FileField(default='media/prod_c8m26c.png', upload_to='media/products/'),
        ),
    ]
