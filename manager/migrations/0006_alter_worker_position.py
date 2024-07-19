# Generated by Django 4.2.13 on 2024-07-19 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0005_alter_worker_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="workers",
                to="manager.position",
                verbose_name="Position",
            ),
        ),
    ]
