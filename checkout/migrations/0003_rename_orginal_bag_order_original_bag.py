# Generated by Django 3.2.25 on 2025-01-07 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20250107_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orginal_bag',
            new_name='original_bag',
        ),
    ]
