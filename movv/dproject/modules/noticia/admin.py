# -*- encoding: utf-8 -*-
################################################################################
# Administração do módulo localizacao
#
# @author: Alexandre Lavarini Matoso
# @since: 04/05/2011
################################################################################

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from futebol.modules.noticia.models import Noticia, NoticiaTime,\
     SourceNoticia, NoticiaTimeView, NoticiaCampeonato, NoticiaCampeonatoView

from unicodedata import normalize

class SourceNoticiaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Noticia'
        
    ordering = ['id_source_noticia']
    search_fields = ('tipo', )
    list_display = ('id_source_noticia', 'tipo', 'idioma', )

class NoticiaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Noticia'
        
    search_fields = ('id_source_noticia__nome', 'url' , 'lead', 'manchete', )
    ordering = ['id_noticia']
    list_display = ('id_noticia', 'id_source_noticia', 'idioma', 'url', 'data',\
                    'lead', 'manchete', 'thumbnail_grande', 'thumbnail_pequeno', 'corpo',\
                    'id_noticia_eusou', 'flag_corpo', )
    raw_id_fields = ('id_source_noticia',)   

class NoticiaTimeAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Noticia Tipo'
        
    ordering = ['id_noticia_time']
    list_display = ('id_noticia_time', )   

class NoticiaTimeViewAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Noticia Tipo View'
        
    ordering = ['id_noticia_time']
    list_display = ('id_noticia_time', 'id_noticia', 'id_time', 'data_insercao', 'visitas', 'last_ip', )  

class NoticiaCampeonatoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Noticia Campeonato'
        
    ordering = ['id_noticia_campeonato']
    list_display = ('id_noticia_campeonato', )   

class NoticiaCampeonatoViewAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Noticia Campeonato View'
        
    ordering = ['id_noticia_campeonato']
    list_display = ('id_noticia_campeonato', 'id_noticia', 'id_campeonato', 'data_insercao', 'visitas',)

admin.site.register(SourceNoticia, SourceNoticiaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(NoticiaTime, NoticiaTimeAdmin)
admin.site.register(NoticiaTimeView, NoticiaTimeViewAdmin)
admin.site.register(NoticiaCampeonato, NoticiaCampeonatoAdmin)
admin.site.register(NoticiaCampeonatoView, NoticiaCampeonatoViewAdmin)