# Generated by Django 4.1.5 on 2023-01-07 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_alter_auction_end_date_alter_auction_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='end_date',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='auction',
            old_name='start_date',
            new_name='start_time',
        ),
    ]
