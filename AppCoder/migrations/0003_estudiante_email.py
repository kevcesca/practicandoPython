# Generated by Django 4.2.4 on 2023-09-05 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0002_estudiante"),
    ]

    operations = [
        migrations.AddField(
            model_name="estudiante",
            name="email",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
