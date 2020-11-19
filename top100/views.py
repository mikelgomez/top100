from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Artista, Album, Estilo, Cancion


def index(request):
	return render(request, 'principal.html')

def albumes(request):
	albums = get_list_or_404(Album.objects.order_by('id'))
	context = {'lista_albums': albums }
	return render(request, 'albumes.html', context)

def detailAlbum(request, album_id):#Para ir desde los albums al album
	album = get_object_or_404(Album, pk=album_id)
	canciones = get_list_or_404(Cancion.objects.order_by('numeroAlbum'), albumCancion=album)
	context = {'album': album, 'canciones' : canciones}
	return render(request, 'detailAlbum.html', context)

def artistas(request):
	artistas = get_list_or_404(Artista.objects.order_by('id'))
	context = {'lista_artistas': artistas }
	return render(request, 'artistas.html', context)

def detailArtista(request, artista_id):#Para ir desde los artistas al artista
	artista = get_object_or_404(Artista, pk=artista_id)
	albumes = get_list_or_404(Album.objects.order_by('nombreAlbum'), artistaAlbum=artista)
	context = {'artista': artista, 'albumes': albumes}
	return render(request, 'detailArtista.html', context)

def port(request):
	return render(request, 'portfolio.html')

def eventos(request):
	return render(request, 'eventos.html')

def equipo(request):
	return render(request, 'equipo.html')

def contacto(request):
	return render(request, 'contacto.html')




#def index(request):#canciones
#	return render(request, 'index.html')

#def index(request):#canciones
#	canciones = get_list_or_404(Cancion.objects.order_by('id'))
#	context = {'lista_canciones': canciones }
#	return render(request, 'index.html', context)

#def detailCancion(request, post_id):#Para ir desde canciones a la cancion especifica
#    cancion = get_object_or_404(Cancion, pk=cancion_id)
#    context = {'cancion': cancion}
#    return render(request, 'detailCancion.html', context) #detail

#def artista(request):#artistas
#	artistas = get_list_or_404(Artista.objects.order_by('id'))
#	context = {'lista_artistas': artistas }
#	return render(request, 'artista.html', context)

#def detailArtista(request, artista_id):#Para ir desde los artistas al artista
#    artista = get_object_or_404(Artista, pk=artista_id)
#    context = {'artista': artista}
#    return render(request, 'detailArtista.html', context)

#def album(request):#albums
#	albums = get_list_or_404(Album.objects.order_by('id'))
#	context = {'lista_albums': albums }
#	return render(request, 'album.html', context)

#def detailAlbum(request, album_id):#Para ir desde los albums al album
#    album = get_object_or_404(Album, pk=album_id)
#    context = {'album': album}
#    return render(request, 'detailAlbum.html', context)

#def estilo(request):#estilos
#	estilos = get_list_or_404(Estilo.objects.order_by('id'))
#	context = {'lista_estilos': estilos }
#	return render(request, 'estilo.html', context)

#def detailEstilo(request, estilo_id):#Para ir desde los estilos al estilo
#    estilo = get_object_or_404(Estilo, pk=estilo_id)
#    context = {'estilo': estilo}
#    return render(request, 'detailEstilo.html', context)