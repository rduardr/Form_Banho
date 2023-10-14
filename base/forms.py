from django import forms
from base.models import Reserva

class ReservaForm(forms.ModelForm):
  class Meta:
    model = Reserva
    fields = ['nome', 'telefone', 'dia', 'observacoes']