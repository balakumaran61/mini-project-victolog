# Generated by Django 4.2.4 on 2023-08-30 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userprofile",
            old_name="phoneno",
            new_name="phone",
        ),
    ]
