# -*- encoding: utf-8 -*-
################################################################################
# Administração do módulo localizacao
#
# @author: Alexandre Lavarini Matoso
# @since: 04/05/2011
################################################################################

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from futebol.modules.time.models import Time, SourceTime, TimeMusica
from crawler_futebol.views import importar_dados_times


from unicodedata import normalize

class TimeAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Time'
        
    search_fields = ('nome_completo', 'nome_popular', 'apelido', 'nome_lista')
    ordering = ['id_time']
    list_display = ('nome_completo', 'nome_popular', 'apelido', 'nome_lista', 'slug',\
                    'nome_torcedor_singular', 'nome_torcedor_plural','tipo', 'id_pais', 'id_estado', 'id_cidade')
    raw_id_fields = ('id_pais', 'id_estado', 'id_cidade',)
    
class SourceTimeAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Time'
        
    ordering = ['id_time', 'id_source_time']
    list_display = ('id_source_time', 'id_time', 'value', 'tipo', )
    raw_id_fields = ('id_time', )
    
    actions = ['importar_dados_times']
    
    def importar_dados_times(self, request, queryset):
        """
        Função que importa dados dos times selecionados
        """
        lista_times = []
        for time in queryset:
            lista_times.append(time)
        importar_dados_times(lista_times=lista_times, tipo_busca='team')
        message_bit = "Os times foram importadas com sucesso"
        self.message_user(request, "%s ." % message_bit)

    importar_dados_times.short_description = 'Atualizar dados times'
    
class TimeMusicaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Time Musica'
        
    search_fields = ('id_time__nome_popular', 'id_time__nome_completo', 'id_time__apelido', 'id_time__nome_lista')
    ordering = ['id_time_musica']
    list_display = ('id_time_musica', 'id_time', 'url', 'tipo', 'id_letra_letrasmusbr',\
                    'id_video_aula', 'ativo')
    raw_id_fields = ('id_time', )

    
admin.site.register(Time, TimeAdmin)
admin.site.register(SourceTime, SourceTimeAdmin)
admin.site.register(TimeMusica, TimeMusicaAdmin)