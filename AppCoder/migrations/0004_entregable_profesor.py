# Generated by Django 4.2.4 on 2023-09-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0003_estudiante_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entregable",
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
                ("nombre", models.CharField(max_length=30)),
                ("fechaDeEntrega", models.DateField()),
                ("entregado", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Profesor",
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
                ("nombre", models.CharField(max_length=30)),
                ("apellido", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30, null=True)),
                ("profesion", models.CharField(max_length=30)),
            ],
        ),
    ]
