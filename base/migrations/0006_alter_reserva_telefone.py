# Generated by Django 4.2.6 on 2023-10-14 19:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_alter_reserva_telefone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserva",
            name="telefone",
            field=models.CharField(
                max_length=12,
                validators=[
                    django.core.validators.RegexValidator(
                        message="O número de telefone deve ser váldio.",
                        regex="^{10,15}$",
                    )
                ],
                verbose_name="Telefone",
            ),
        ),
    ]
