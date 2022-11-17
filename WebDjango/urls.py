from django.urls import path
from WebDjango.views import *



urlpatterns = [
    path("inicio/", inicio, name="proyecto-inicio"),
    path("peliculas/", peliculas, name="proyecto-peliculas"),
    path("peliculas/crear/", creacion_pelicula, name="proyecto-peliculas-crear"),
    path("peliculas/buscar/", buscar_pelicula, name="proyecto-peliculas-buscar"),
    path("peliculas/buscar/resultados", resultados_busqueda_peliculas, name="proyecto-peliculas-buscar-resultados"),
    path("series/", series, name="proyecto-series"),
    path("series/crear/", creacion_serie, name="proyecto-series-crear"),
    path("music/", music, name="proyecto-music"),
    path("music/crear/", creacion_musica, name="proyecto-music-crear"),

]