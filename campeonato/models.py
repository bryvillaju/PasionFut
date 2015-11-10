from django.db import models
from django.utils import timezone

class Partido(models.Model):
    Publicador = models.ForeignKey('auth.User')
    Equipo1 = models.CharField(max_length=200)
    Equipo2 = models.CharField(max_length=200)
    GolesEquipo1=models.CharField(max_length=3)
    GolesEquipo2=models.CharField(max_length=3)
    Resumen = models.TextField()
    Fecha_Publicacion = models.DateTimeField(
    default=timezone.now)
    Fecha_Partido = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.Fecha_Partido = timezone.now()
        self.save()

    def __str__(self):
        return self.title
