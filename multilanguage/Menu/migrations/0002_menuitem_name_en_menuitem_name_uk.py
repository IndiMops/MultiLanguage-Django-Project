# Generated by Django 5.0.6 on 2024-05-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Menu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="name_en",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="name_uk",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
