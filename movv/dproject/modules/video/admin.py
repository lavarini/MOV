# -*- encoding: utf-8 -*-
################################################################################
# Administração do módulo localizacao
#
# @author: Alexandre Lavarini Matoso
# @since: 04/05/2011
################################################################################

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from futebol.modules.video.models import SourceVideo, VideoCategoria,\
     Video, VideoTime, VideoPessoa, VideoEventoJogo

from unicodedata import normalize

class SourceVideoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Video'
        
    ordering = ['id_source_video']
    search_fields = ('tipo', )
    list_display = ('id_source_video', 'tipo', 'idioma', )

class VideoCategoriaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Video Categoria'
        
    search_fields = ('nome', )
    ordering = ['id_video_categoria']
    list_display = ('id_video_categoria', 'nome', 'slug', ) 

class VideoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Video'
        
    search_fields = ('id_source_video__tipo', 'id_video_categoria__nome' , 'titulo', )
    ordering = ['id_video']
    list_display = ('id_video', 'id_source_video', 'id_video_categoria', 'idioma', 'url',\
                    'data', 'titulo', 'descricao', 'duracao', 'thumbnail_grande',\
                    'thumbnail_pequeno', 'id_video_eusou', )

class VideoTimeAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Video Time'
        
    ordering = ['id_video_time']
    list_display = ('id_video_time', 'id_video', 'id_time', 'data_insercao',\
                    'visualizacoes', 'last_ip') 
    raw_id_fields = ('id_video', 'id_time', )  

class VideoPessoaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Video Pessoa'
        
    ordering = ['id_video_pessoa']
    list_display = ('id_video_pessoa', 'id_video', 'id_pessoa', 'data_insercao',\
                    'visualizacoes', )  
    raw_id_fields = ('id_video', 'id_pessoa', )

class VideoEventoJogoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Video Evento Jogo'
        
    ordering = ['id_video_evento_jogo']
    list_display = ('id_video_evento_jogo', 'id_video', 'id_evento_jogo', 'data_insercao',\
                    'visualizacoes', )  
    raw_id_fields = ('id_video', 'id_evento_jogo', )  


admin.site.register(SourceVideo, SourceVideoAdmin)
admin.site.register(VideoCategoria, VideoCategoriaAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoTime, VideoTimeAdmin)
admin.site.register(VideoPessoa, VideoPessoaAdmin)
admin.site.register(VideoEventoJogo, VideoEventoJogoAdmin)