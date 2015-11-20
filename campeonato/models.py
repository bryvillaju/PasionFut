from django.db import models
from django.utils import timezone

class Partido(models.Model):
    Publicador = models.ForeignKey('auth.User')
    Equipo1 = models.CharField(max_length=200)
    Equipo2 = models.CharField(max_length=200)
    GolesEquipo1=models.CharField(max_length=3,blank=True, null=True)
    GolesEquipo2=models.CharField(max_length=3,blank=True, null=True)
    Resumen = models.TextField(blank=True, null=True)
    Fecha_Publicacion = models.DateTimeField(
    default=timezone.now)
    Fecha_Partido = models.DateTimeField()

    def publicar(self):
        self.Fecha_Partido = timezone.now()
        self.save()

    def __str__(self):
        return self.Equipo1+' - '+self.Equipo2
