from django.db import models

# Create your models here.

class Artista(models.Model):
    nombreArtista = models.CharField(max_length = 50)
    descripcionArtista = models.TextField()
    imagenArtista = models.CharField(max_length = 200)
    albumArtista = models.ManyToManyField(Album, on_delete = models.Cascade)
    cancionArtista = models.ManyToManyField(Cancion, on_delete = models.Cascade)
class Album(models.Model):
    nombreAlbum = models.CharField(max_length=50)
    imagenAlbum = models.CharField(max_length=200)
    artistaAlbum = models.ForeignKey(Artista)
    estiloAlbum = models.ForeignKey(Estilo)
    cancionAlbum = models.ManyToManyField(Cancion, on_delete = models.Cascade)


class Estilo(models.Model):
    nombreEstilo = models.CharField(max_length = 50)
    imagenEstilo = models.CharField(max_length = 200)
    albumEstilo = models.ManyToManyField(Album, on_delete = models.Cascade)
    cancionEstilo = models.ManyToManyField(Cancion, on_delete = models.Cascade)

class Cancion(models.Model):
    nombreCancion = models.CharField(max_length = 50)
    videoCancion = models.CharField(max_length = 300)#Al entrar en carac. saque un video de esa cancion
    albumCancion = models.ForeignKey(Album)
    estiloCancion = models.ForeignKey(Estilo)
    artistaCancion = models.ForeignKey(Artista)
