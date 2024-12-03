# Generated by Django 5.1.3 on 2024-11-28 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_customuser_is_active_customuser_is_staff_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name_plural": "Addresses"},
        ),
        migrations.AlterField(
            model_name="customuser",
            name="website",
            field=models.URLField(
                default="",
                validators=[
                    django.core.validators.RegexValidator(
                        message="Enter a valid website URL.",
                        regex="^(https?://)?(www\\.)?([a-zA-Z0-9-]+)\\.[a-zA-Z]{2,}(?:/.*)?$",
                    )
                ],
            ),
        ),
    ]
