from django.shortcuts import render, redirect
from base.forms import ReservaForm

def reserva(request):
  sucesso = False
  if request.method == 'POST':
    form = ReservaForm(request.POST)
    if form.is_valid():
      sucesso = True
      form.save()
      return redirect(success)
  else:
      form = ReservaForm()

  contexto = {
     'form': form,
     'sucesso': sucesso,
  }
  return render(request, 'reserva.html', contexto)

from django.shortcuts import render

def success(request):
    return render(request, 'success.html')
