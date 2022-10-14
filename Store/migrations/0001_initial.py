# Generated by Django 4.1.2 on 2022-10-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("store", models.CharField(max_length=128, unique=True)),
                ("owner", models.CharField(max_length=128)),
            ],
        ),
    ]
