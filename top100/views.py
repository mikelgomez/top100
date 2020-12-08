from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Artista, Album, Estilo, Cancion
from .forms import MyForm


def index(request):
	return render(request, 'principal.html')

def albumes(request):
	albums = get_list_or_404(Album.objects.order_by('id'))
	context = {'lista_albums': albums }
	return render(request, 'albumes.html', context)

def detailAlbum(request, album_id):#Para ir desde los albums al album
	album = get_object_or_404(Album, pk=album_id)
	canciones = get_list_or_404(Cancion.objects.order_by('numeroRanking'), albumCancion=album)
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

def estilos(request):
	estilos = get_list_or_404(Estilo.objects.order_by('nombreEstilo'))
	albumes = get_list_or_404(Album.objects.order_by('estiloAlbum'))
	context = {'estilos': estilos, 'albumes': albumes}
	return render(request, 'estilos.html', context)

def detailEstilo(request, estilo_id):#Para ir desde los estilos al estilo
	estilo = get_object_or_404(Estilo, pk=estilo_id)
	albumes = get_list_or_404(Album.objects.order_by('nombreAlbum'), estiloAlbum=estilo)
	context = {'estilo': estilo, 'albumes' : albumes}
	return render(request, 'detailEstilo.html', context)

def detailCancion(request, cancion_id):#Para ir desde canciones a la cancion especifica
    cancion = get_object_or_404(Cancion, pk=cancion_id)
    context = {'cancion': cancion}
    return render(request, 'detailCancion.html', context) #detail

def ranking(request):
	canciones = get_list_or_404(Cancion.objects.order_by('numeroRanking'))
	context = {'canciones': canciones}
	return render(request, 'ranking.html', context)

def equipo(request):
	return render(request, 'equipo.html')

def contacto(request):
	return render(request, 'contacto.html')

def home(request):#canciones
	canciones = get_list_or_404(Cancion.objects.order_by('numeroRanking'))
	estilos = get_list_or_404(Estilo.objects.order_by('nombreEstilo'))
	cancionesPorEstilo = list()
	for e in estilos:
		numCanciones=0
		for c in canciones:
			if c.estiloCancion == e and numCanciones<2:
				cancionesPorEstilo.append(c)
				numCanciones = numCanciones+1

	context = {'cancionesPorEstilo': cancionesPorEstilo, 'estilos':estilos}
	return render(request, 'home.html', context)


def loginform(request):
 form = MyForm()
 return render(
 request, 'contacto.html', {'form':form}
 )
def get_name(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']   
			email = form.cleaned_data['email']
			mensaje=form.cleaned_data['mensaje']
			return HttpResponseRedirect('/dashboard/')
	else:
		form = NameForm()
	return render(request, 'Contacto.html', {'form': form})

def idiomas(request):
	return render(request, 'idiomas.html')
#def detailCancion(request, post_id):#Para ir desde canciones a la cancion especifica
#    cancion = get_object_or_404(Cancion, pk=cancion_id)
#    context = {'cancion': cancion}
#    return render(request, 'detailCancion.html', context) #detail
