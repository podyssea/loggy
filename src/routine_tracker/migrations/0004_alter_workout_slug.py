# Generated by Django 4.2.5 on 2023-10-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("routine_tracker", "0003_workout_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workout",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]