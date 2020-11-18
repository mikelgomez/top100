from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('cancion', views.cancion, name='cancion'), #todas las canciones
   path('artista', views.artista, name='artista'), #todos los artistas
   path('album', views.album, name='album'), #todos los albums
   path('estilo', views.estilo, name='estilo'), #todos los estilos
   path('cancion/<int:cancion_id>/cancionPost', views.detailCancion, name='detailCancion'), #detalles de canciones
   path('artista/<int:artista_id>/detailArtistas', views.detailAutor, name='detailAutor'), #detalles de artistas
   path('album/<int:album_id>/detailAlbum', views.detailAlbum, name='detailAlbum'), #detalles de albumes
   path('estilo/<int:estilo_id>/detailEstilo', views.detailEstilo, name='detailEstilo') #detalles de estilos
   #path('acerca', views.acerca, name= 'acerca'),
   #path('contacto', views.contacto, name = 'contacto')
    
]