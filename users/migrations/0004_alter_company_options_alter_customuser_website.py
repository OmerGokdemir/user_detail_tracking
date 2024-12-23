# Generated by Django 5.1.3 on 2024-11-28 16:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_address_options_alter_customuser_website"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"verbose_name_plural": "Companies"},
        ),
        migrations.AlterField(
            model_name="customuser",
            name="website",
            field=models.URLField(
                default="",
                validators=[
                    django.core.validators.RegexValidator(
                        message="Enter a valid website URL.",
                        regex="^(https?://)?(www\\.)?([a-zA-Z0-9-]+)\\.[a-zA-Z]{2,}\\.[a-zA-Z]{2,}(?:/.*)?$",
                    )
                ],
            ),
        ),
    ]
