# Generated by Django 4.2.13 on 2024-05-21 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0003_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(blank=True, to="manager.tag"),
        ),
    ]
