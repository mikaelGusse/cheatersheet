# Generated by Django 4.2.18 on 2025-03-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cheatersheet", "0006_remove_case_data_blocks_datablock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datablock",
            name="data_type",
            field=models.IntegerField(
                choices=[(0, "Free Text"), (1, "Code Showcase"), (2, "Timeline")],
                default=0,
            ),
        ),
    ]
