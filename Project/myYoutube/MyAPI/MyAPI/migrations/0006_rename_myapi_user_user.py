# Generated by Django 4.2 on 2023-04-21 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyAPI', '0005_rename_test_myapi_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyAPI_user',
            new_name='User',
        ),
    ]