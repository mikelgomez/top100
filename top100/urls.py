from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('albumes/', views.albumes, name='albumes'),
   path('albumes/<int:album_id>', views.detailAlbum, name='detailAlbum'), #detalles de albumes
   path('artistas/', views.artistas, name='artistas'),
   path('artistas/<int:artista_id>', views.detailArtista, name='detailArtista'), #detalles de artistas
   path('estilos/', views.estilos, name='estilos'),
   path('estilos/<int:estilo_id>', views.detailEstilo, name='detailEstilo'), #detalles de estilos
   path('eventos/', views.eventos, name='eventos'),
   path('equipo/', views.equipo, name='equipo'),
   path('contacto/', views.contacto, name='contacto'),
   path('canciones/', views.index, name='canciones'), #todas las canciones
   path('canciones/<int:cancion_id>', views.detailCancion, name='detailCancion'), #detalles de canciones

   #path('artista', views.artista, name='artista'), #todos los artistas
   #path('album', views.album, name='album'), #todos los albums
   #path('acerca', views.acerca, name= 'acerca'),
   #path('contacto', views.contacto, name = 'contacto')
    
]