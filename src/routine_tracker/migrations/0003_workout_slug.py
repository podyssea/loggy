# Generated by Django 4.2.5 on 2023-10-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("routine_tracker", "0002_workout_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="workout",
            name="slug",
            field=models.SlugField(default="hello world"),
            preserve_default=False,
        ),
    ]
