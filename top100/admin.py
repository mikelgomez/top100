from django.contrib import admin
from .models import Cancion, Album, Estilo, Artista
class QuestionAdminArtista(admin.ModelAdmin):
    #fieldsets = [
    #    ('Information del Artista', {'fields': ['nombreArtista']}),
    #    (None, {'fields': ['descripcionArtista']}),
    #    (None, {'fields': ['imagenArtista']})
    #]

    list_display = ('nombreArtista', 'descripcionArtista', 'imagenArtista')
    list_editable = ['imagenArtista']
    search_fields = ['nombreArtista']
    list_filter = ['nombreArtista']
    list_per_page = 2
    
class QuestionAdminEstilo(admin.ModelAdmin):
    #fieldsets = [
    #    ('Information del Estilo', {'fields': ['nombreEstilo']}),
    #    (None, {'fields': ['imagenEstilo']}),
    #    (None, {'fields': ['descripcionEstilo']})
    #]

    list_display = ('nombreEstilo','imagenEstilo', 'descripcionEstilo')
    list_editable = ['imagenEstilo']
    search_fields = ['nombreEstilo']
    list_filter = ['nombreEstilo']
    list_per_page = 2

class QuestionAdminAlbum(admin.ModelAdmin):
    #fieldsets = [
    #    ('Information del Album', {'fields': ['nombreAlbum']}),
    #    (None, {'fields': ['imagenAlbum']}),
    #    (None, {'fields': ['descripcionAlbum']}),
    #    (None, {'fields': ['artistaAlbum']}),
    #    (None, {'fields': ['estiloAlbum']})
    #]

    list_display = ('nombreAlbum','imagenAlbum', 'descripcionAlbum', 'artistaAlbum', 'estiloAlbum')
    list_editable = ['imagenAlbum', 'artistaAlbum','estiloAlbum']
    search_fields = ['nombreAlbum']
    list_filter = ['nombreAlbum','artistaAlbum','estiloAlbum']
    list_per_page = 2

class QuestionAdminCancion(admin.ModelAdmin):
    #fieldsets = [
    #    ('Information de la Cancion', {'fields': ['nombreCancion']}),
    #    (None, {'fields': ['videoCancion']}),
    #    (None, {'fields': ['numeroRanking']}),
    #    (None, {'fields': ['albumCancion']}),
    #    (None, {'fields': ['estiloCancion']}),
    #    (None, {'fields': ['artistaCancion']})
    #]

    list_display = ('nombreCancion','videoCancion', 'numeroRanking', 'albumCancion', 'estiloCancion','artistaCancion')
    list_editable = ['numeroRanking','albumCancion','estiloCancion','artistaCancion']
    search_fields = ['nombreCancion']#solo se puede buscar por nombre
    list_filter = ['albumCancion','estiloCancion','artistaCancion']
    list_per_page = 4

admin.site.register(Artista, QuestionAdminArtista)
admin.site.register(Cancion, QuestionAdminCancion)
admin.site.register(Album, QuestionAdminAlbum)
admin.site.register(Estilo, QuestionAdminEstilo)
# Register your models here.