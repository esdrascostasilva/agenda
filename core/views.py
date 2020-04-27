from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

# uma das maneiras de direciona para agenda com a URL mãe
def index(request):
    return redirect('/agenda')

def lista_eventos(request):
    # retornaria no html apenas o evento do ID 1
    # evento = Evento.objects.get(id=1)

    # retorna todos os eventos
    evento = Evento.objects.all()

    usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}

    return render(request, 'agenda.html', dados)