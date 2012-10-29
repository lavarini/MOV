# -*- encoding: utf-8 -*-
################################################################################
# Administração do módulo localizacao
#
# @author: Alexandre Lavarini Matoso
# @since: 26/04/2010
################################################################################

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from futebol.modules.localizacao.models import Continente, Pais,\
    Estado, Cidade, SourcePais
from futebol.utils import importar_paises, importar_cidades 
from crawler_futebol.views import importar_areas, importar_estadios

from unicodedata import normalize

class ContinenteAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Continentes'
        
    search_fields = ('nome_pt', 'nome_confederacao', 'sigla')
    list_filter = ('nome_confederacao', )
    ordering = ['nome_pt']
    list_display = ('id_continente', 'nome_pt', 'nome_en', 'nome_es', 'nome_confederacao', 'sigla', )
    actions = ['importar_paises', 'importar_cidades']
    
    def importar_paises(self, request, queryset):
        """
        Função que ativa todos campeonatos selecionados
        """
        importar_paises()
        
        self.message_user(request, "Os paises foram importados com sucesso.")

    importar_paises.short_description = 'Importar paises'
    
    def importar_cidades(self, request, queryset):
        """
        Função que ativa todos campeonatos selecionados
        """
        importar_cidades()
        
        self.message_user(request, "As cidades foram importados com sucesso.")

    importar_cidades.short_description = 'Importar cidades'
    
class PaisAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Paises'
        
    search_fields = ('id_continente__nome_pt', 'nome_pt', 'iso3', 'iso')
    list_filter = ('id_continente__nome_pt', )
    ordering = ['id_continente__nome_pt', 'nome_pt']
    list_display = ('id_pais', 'id_continente', 'nome_pt', 'nome_en',\
                    'nome_es', 'area', 'populacao', 'iso3', 'iso', 'tld',\
                    'codigo_moeda', 'nome_moeda', 'telefone')
    
    actions = ['importar_areas', 'importar_estadios']
    
    def importar_areas(self, request, queryset):
        """
        Função que ativa todos campeonatos selecionados
        """
        importar_areas()
        
        self.message_user(request, "As areas foram importados com sucesso.")

    importar_areas.short_description = 'Importar areas'
    
    def importar_estadios(self, request, queryset):
        """
        Função que importa todos estadios dos paises escolhidos
        """
        pais_fonte = ''
        for pais in queryset:
            fonte_pais = SourcePais.objects.filter(id_pais=pais.id_pais)
            if not fonte_pais:
                if pais_fonte:
                    pais_fonte += ', '
                pais_fonte += normalize('NFKD', pais.nome_pt).encode('ASCII', 'ignore')
        if pais_fonte:
            message_bit = "Os paises %s não possuem relação fonte"%(pais_fonte)
            self.message_user(request, "%s ." % message_bit)
        else:
            lista_paises = []
            for pais in queryset:
                fonte_pais = SourcePais.objects.get(id_pais=pais.id_pais)
                lista_paises.append(fonte_pais)
            importar_estadios(lista_paises=lista_paises, tipo_busca='area')
            message_bit = "Os estadios foram importadas com sucesso"
            self.message_user(request, "%s ." % message_bit)

    importar_estadios.short_description = 'Importar/Atualizar estadios'
    
class SourcePaisAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Paises'
        
    search_fields = ('id_pais__nome', )
    ordering = ['id_pais', 'id_source_pais']
    list_display = ('id_source_pais', 'id_pais', 'value', 'tipo', )
    raw_id_fields = ('id_pais', )

class EstadoAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Estados'
        
    search_fields = ('id_pais__nome_pt', 'nome', 'slug')
    list_filter = ('id_pais__nome_pt', )
    ordering = ['id_pais__nome_pt' ,'nome']
    list_display = ('id_estado', 'id_pais', 'nome', 'slug', )

class CidadeAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Estados'
        
    search_fields = ('id_estado__nome', 'nome', )
    list_filter = ('id_estado__nome', )
    ordering = ['id_estado__nome' ,'nome']
    list_display = ('id_cidade', 'id_estado', 'nome', 'capital', )

admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(SourcePais, SourcePaisAdmin)
admin.site.register(Continente, ContinenteAdmin)