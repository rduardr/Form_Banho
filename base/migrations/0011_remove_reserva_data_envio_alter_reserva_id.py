# Generated by Django 4.2.6 on 2023-10-14 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0010_reserva_data_envio_alter_reserva_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reserva",
            name="data_envio",
        ),
        migrations.AlterField(
            model_name="reserva",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
