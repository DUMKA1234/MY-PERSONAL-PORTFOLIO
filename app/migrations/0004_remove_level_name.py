# Generated by Django 5.1.4 on 2025-01-13 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='name',
        ),
    ]
