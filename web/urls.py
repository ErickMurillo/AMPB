from django.urls import path
from .views import *

urlpatterns = [
    path('noticias/', lista_noticias, name='lista-noticias'),
    path('noticias/por-pais/<slug>', filtro_noticias, name='filtro-noticias'),
    path('noticias/<slug>', detalle_noticia, name='detalle-noticia'),
    path('galerias/', lista_galerias, name='lista-galerias'),
    path('galerias/por-pais/<slug>', filtro_galerias, name='filtro-galerias'),
    path('galerias/<slug>', detalle_galeria, name='detalle-galeria'),
    path('eventos/', lista_eventos, name='lista-eventos'),
    path('eventos/por-pais/<slug>', filtro_eventos, name='filtro-eventos'),
    path('eventos/<slug>', detalle_evento, name='detalle-evento'),
    path('biblioteca/', lista_biblioteca, name='lista-biblioteca'),
    # path('biblioteca/por-pais/<slug>', filtro_biblioteca, name='filtro-biblioteca'),
]