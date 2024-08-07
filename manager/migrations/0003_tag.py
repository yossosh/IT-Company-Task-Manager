# Generated by Django 4.2.13 on 2024-05-21 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0002_alter_worker_position"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Tag Name")),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
                "ordering": ["name"],
            },
        ),
    ]
