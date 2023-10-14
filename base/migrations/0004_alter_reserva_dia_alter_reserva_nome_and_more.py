# Generated by Django 4.2.6 on 2023-10-12 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_reserva_dia_alter_reserva_nome_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserva",
            name="dia",
            field=models.CharField(
                choices=[
                    ("segunda", "Segunda"),
                    ("terça", "Terça"),
                    ("quarta", "Quarta"),
                    ("quinta", "Quinta"),
                    ("sexta", "Sexta"),
                    ("sábado", "Sábado"),
                ],
                max_length=12,
                verbose_name="Dia da Reserva",
            ),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="nome",
            field=models.CharField(max_length=50, verbose_name="Nome do Pet"),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="telefone",
            field=models.CharField(max_length=12, verbose_name="Telefone"),
        ),
    ]