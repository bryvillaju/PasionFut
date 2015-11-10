# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Equipo1', models.CharField(max_length=200)),
                ('Equipo2', models.CharField(max_length=200)),
                ('GolesEquipo1', models.CharField(max_length=3)),
                ('GolesEquipo2', models.CharField(max_length=3)),
                ('Resumen', models.TextField()),
                ('Fecha_Publicacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('Fecha_Partido', models.DateTimeField(null=True, blank=True)),
                ('Publicador', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
