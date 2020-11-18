from django.contrib import admin
from .models import Cancion, Album, Estilo, Artista

# Register your models here.
admin.site.register(Cancion)
admin.site.register(Album)
admin.site.register(Estilo)
admin.site.register(Artista)