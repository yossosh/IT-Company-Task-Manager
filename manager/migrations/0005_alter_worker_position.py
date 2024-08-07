# Generated by Django 4.2.13 on 2024-06-06 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0004_task_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                default=16,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="workers",
                to="manager.position",
                verbose_name="Position",
            ),
        ),
    ]
