# Generated by Django 5.0.3 on 2024-03-08 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investing_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Investimento',
            new_name='Investment',
        ),
    ]