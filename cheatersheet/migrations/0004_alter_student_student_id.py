# Generated by Django 4.2.18 on 2025-03-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cheatersheet", "0003_alter_case_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(
                default="", help_text="Student number", max_length=255
            ),
        ),
    ]
