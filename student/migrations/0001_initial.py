# Generated by Django 5.0 on 2024-01-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("fname", models.CharField(max_length=25)),
                ("lname", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=25)),
                ("phone", models.PositiveIntegerField()),
                (
                    "branch",
                    models.CharField(
                        choices=[
                            ("choice1", "CE"),
                            ("choice2", "EXTC"),
                            ("choice3", "ME"),
                            ("choice4", "AI"),
                            ("choice5", "IT"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
