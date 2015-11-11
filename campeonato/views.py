from django.shortcuts import render

def lista_partidos(request):
    return render(request, 'campeonato/lista_partidos.html', {})
