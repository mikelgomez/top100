from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('cancion', views.index, name='cancion'), #todas las canciones
   path('artista', views.artista, name='artista'), #todos los artistas
   path('album', views.album, name='album'), #todos los albums
   path('estilo', views.estilo, name='estilo'), #todos los estilos
   path('cancion/<int:cancion_id>', views.detailCancion, name='detailCancion'), #detalles de canciones
   path('artista/<int:artista_id>', views.detailArtista, name='detailArtistaS'), #detalles de artistas
   path('album/<int:album_id>', views.detailAlbum, name='detailAlbum'), #detalles de albumes
   path('estilo/<int:estilo_id>', views.detailEstilo, name='detailEstilo') #detalles de estilos
   #path('acerca', views.acerca, name= 'acerca'),
   #path('contacto', views.contacto, name = 'contacto')
    
]