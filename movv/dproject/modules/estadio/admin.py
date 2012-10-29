# -*- encoding: utf-8 -*-
################################################################################
# Administração do módulo localizacao
#
# @author: Alexandre Lavarini Matoso
# @since: 02/05/2011
################################################################################

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from futebol.modules.estadio.models import Estadio, SourceEstadio,\
     EstadioTime

from unicodedata import normalize

class EstadioAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Estadio'
        
    search_fields = ('nome', 'nome_popular')
    ordering = ['id_cidade__nome' ,'nome']
    list_display = ('id_estadio', 'nome', 'nome_popular', 'id_cidade', )
    raw_id_fields = ('id_cidade',)
    
class SourceEstadioAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Estadio'
        
    search_fields = ('id_estadio__nome', 'value')
    ordering = ['id_estadio', 'id_source_estadio']
    list_display = ('id_source_estadio', 'id_estadio', 'value', 'tipo', )
    raw_id_fields = ('id_estadio', )
    
class EstadioTimeAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Estadio Time'
        
    search_fields = ('id_time__nome_popular', )
    ordering = ['id_time', 'id_estadio_time']
    list_display = ('id_estadio_time', 'id_time', 'id_estadio', )
    raw_id_fields = ('id_time', 'id_estadio', )


admin.site.register(Estadio, EstadioAdmin)
admin.site.register(SourceEstadio, SourceEstadioAdmin)
admin.site.register(EstadioTime, EstadioTimeAdmin)