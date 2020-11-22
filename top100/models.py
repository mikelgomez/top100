from django.db import models

# Create your models here.

class Artista(models.Model):
    nombreArtista = models.CharField(max_length = 50)
    descripcionArtista = models.TextField()
    imagenArtista = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombreArtista

class Estilo(models.Model):
    nombreEstilo = models.CharField(max_length = 50)
    imagenEstilo = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombreEstilo

class Album(models.Model):
    nombreAlbum = models.CharField(max_length=50)
    imagenAlbum = models.CharField(max_length=200)
    descripcionAlbum = models.TextField(null = True)
    artistaAlbum = models.ForeignKey(Artista, on_delete=models.CASCADE)
    estiloAlbum = models.ForeignKey(Estilo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreAlbum

class Cancion(models.Model):
    nombreCancion = models.CharField(max_length = 50)
    videoCancion = models.CharField(max_length = 300)#Al entrar en carac. saque un video de esa cancion
    numeroRanking = models.IntegerField(default=0)
    albumCancion = models.ForeignKey(Album, on_delete=models.CASCADE)
    estiloCancion = models.ForeignKey(Estilo, on_delete=models.CASCADE)
    artistaCancion = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        cadena = str(self.numeroRanking)+') '+self.nombreCancion
        return cadena