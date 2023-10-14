from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Reserva(models.Model):

  DIAS_CHOICES = (
    ('segunda', 'Segunda'),
    ('terça', 'Terça'),
    ('quarta', 'Quarta'),
    ('quinta', 'Quinta'),
    ('sexta', 'Sexta'),
    ('sábado', 'Sábado'),
  )
    
  nome = models.CharField(verbose_name='Nome do Pet', max_length=50,)
  telefone = models.CharField(verbose_name='Telefone', max_length=11, validators=[RegexValidator(regex='^[0-9]{11,11}$', message='O número de telefone deve conter 11 dígitos numéricos.')])
  dia = models.CharField(verbose_name='Dia da Reserva', max_length=12, choices=DIAS_CHOICES)
  observacoes = models.TextField(blank=True)
