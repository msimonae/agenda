from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.
#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):

    # lista todos os registros
    evento = Evento.objects.all

    #usuario = request.user
    # Lista apenas os registro do usuário logado em site/admin
    #evento = Evento.objects.filter(usuario=usuario)

    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

