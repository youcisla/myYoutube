# Generated by Django 4.2 on 2023-04-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('role', models.IntegerField(max_length=1)),
                ('email', models.CharField(max_length=20)),
                ('Adresse', models.CharField(max_length=20)),
            ],
        ),
    ]
