# Generated by Django 3.2.25 on 2025-01-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_userprofile_default_county'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
