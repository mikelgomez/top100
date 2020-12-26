from django.urls import include, path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('albumes/', views.albumes, name='albumes'),
   path('albumes/<int:album_id>', views.detailAlbum, name='detailAlbum'), #detalles de albumes
   path('artistas/', views.artistas, name='artistas'),
   path('artistas/<int:artista_id>', views.detailArtista, name='detailArtista'), #detalles de artistas
   path('estilos/', views.estilos, name='estilos'),
   path('estilos/<int:estilo_id>', views.detailEstilo, name='detailEstilo'), #detalles de estilos
   path('ranking/', views.ranking, name='ranking'),#ranking
   path('equipo/', views.equipo, name='equipo'),
   path('contacto/', views.contacto, name='contacto'),
   path('canciones/', views.home, name='canciones'), #todas las canciones
   path('canciones/<int:cancion_id>', views.detailCancion, name='detailCancion'), #detalles de canciones
   path('cancionesAjax/<int:cancion_id>', views.ajax, name='ajax'),

   path('i18n/', include('django.conf.urls.i18n')),

   #path('artista', views.artista, name='artista'), #todos los artistas
   #path('album', views.album, name='album'), #todos los albums
   #path('acerca', views.acerca, name= 'acerca'),
   #path('contacto', views.contacto, name = 'contacto')
    
]