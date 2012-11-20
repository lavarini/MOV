# -*- encoding: utf-8 -*-
################################################################################
# Administração do módulo pacientes
#
# @author: Alexandre Lavarini Matoso
# @since: 31/03/2011
################################################################################
import datetime
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from dproject.modules.leite.models import LeitePrimario, LeiteFinal
from django.contrib.admin import SimpleListFilter

class LeitePrimarioAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Leite Primario'

    #form = FontesCampeonatosForm
    search_fields = ('id_doador__nome', 'id_doador__prontuario', 'data', 'id_doador__cpf', 'id_doador__rg', 'classificacao',)
    ordering = ['-id_leite']
    list_display = ('id_doador', 'identificador', 'quantidade', 'classificacao', 'data', 'pasteurizado',)
    list_filter = ('quantidade', 'classificacao', )
    raw_id_fields = ('id_doador', )

class LeiteFinalAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Leite Final'

    #form = FontesCampeonatosForm
    search_fields = ('id_leite_primario__id_doador__nome', 'id_leite_primario__identificador', 'identificador', 
                     'id_leite_primario__id_doador__prontuario', 'data', 'id_leite_primario__id_doador__cpf', 
                     'classificacao',)
    ordering = ['-id_leite_final']
    list_display = ('identificador', 'quantidade', 'classificacao', 'data', )
    list_filter = ('quantidade', 'classificacao', )
    filter_horizontal = ('id_leite_primario',)

admin.site.register(LeiteFinal, LeiteFinalAdmin)
admin.site.register(LeitePrimario, LeitePrimarioAdmin)

