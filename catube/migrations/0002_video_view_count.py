# Generated by Django 3.1 on 2020-08-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catube", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="view_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
