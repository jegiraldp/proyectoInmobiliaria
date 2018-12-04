from django.shortcuts import render
from django.http import HttpResponse
from .forms import personaForm
from .models import persona


def index(request):
    ctx={'info':'Bienvenidos'}
    return render (request,"bienes/inicio.html",ctx)

def personasForm(request):
    if request.method == 'POST':
        form = personaForm(request.POST)
        if form.is_valid():
            form.save()
            #ctx={'form':form}
            return HttpResponse('Registro ok')
    form = personaForm()
    ctx={'form':form}
    return render (request,"bienes/formulario.html",ctx)

def getpersonas(request):
    lista = persona.objects.order_by('documento')
    ctx = {'personas': lista}
    return render (request,"bienes/listadoPersonas.html",ctx)