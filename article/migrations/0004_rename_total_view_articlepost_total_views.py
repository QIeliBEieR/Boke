# Generated by Django 4.2.3 on 2023-08-12 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_articlepost_total_view'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepost',
            old_name='total_view',
            new_name='total_views',
        ),
    ]
