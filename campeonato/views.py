from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Partido
from django.shortcuts import render, get_object_or_404
from .forms import PartidoForm


def lista_partidos(request):
    partidos = Partido.objects.order_by('-Fecha_Partido')
    return render(request, 'campeonato/lista_partidos.html', {'partidos': partidos})

def detalle_partido(request,pk):
    partido=get_object_or_404(Partido,pk=pk)
    return render(request, 'campeonato/detalle_partido.html', {'partido': partido})

@login_required
def nuevo_partido(request):
    if request.method == "POST":
        form = PartidoForm(request.POST)
        if form.is_valid():
            partido = form.save(commit=False)
            partido.Publicador = request.user
            partido.save()
            return redirect('campeonato.views.detalle_partido', pk=partido.pk)
    else:
        form = PartidoForm()
    return render(request, 'campeonato/editar_partido.html', {'form': form})    

@login_required
def editar_partido(request, pk):
    partido = get_object_or_404(Partido, pk=pk)
    if request.method == "POST":
        form = PartidoForm(request.POST, instance=partido)
        if form.is_valid():
            partido = form.save(commit=False)
            partido.Publicador = request.user
            partido.save()
            return redirect('campeonato.views.detalle_partido', pk=partido.pk)
    else:
        form = PartidoForm(instance=partido)
    return render(request, 'campeonato/editar_partido.html', {'form': form})

@login_required
def eliminar_partido(request, pk):
    partido = get_object_or_404(Partido, pk=pk)
    partido.delete()
    return redirect('campeonato.views.lista_partidos')
