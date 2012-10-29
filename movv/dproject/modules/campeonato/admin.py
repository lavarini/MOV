# -*- encoding: utf-8 -*-
################################################################################
# Administração do módulo localizacao
#
# @author: Alexandre Lavarini Matoso
# @since: 04/05/2011
################################################################################

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from futebol.modules.campeonato.models import Campeonato, Temporada,\
     CampeonatoFaseTipo, CampeonatoFase, SourceCampeonatoFase,\
     SourceCampeonato, CampeonatoFaseGrupo, CampeonatoFaseGrupoTabela
from crawler_futebol.views import importar_jogos, importar_pessoas,\
     importar_rodada, importar_dados_pessoas, importar_jogos_live

from unicodedata import normalize

class TemporadaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Temporada'
        
    ordering = ['id_temporada']
    list_display = ('id_temporada', 'data_inicio', 'data_fim', )

class CampeonatoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Campeonato'
        
    search_fields = ('slug', )
    list_filter = ('id_temporada__data_inicio', )
    ordering = ['-id_temporada', 'id_campeonato']
    list_display = ('id_campeonato', 'nome', 'slug', 'data_inicio', 'data_fim', 'ativo_set', )
    raw_id_fields = ('id_temporada', )
    
    actions = ['importar_jogos', 'importar_pessoas' ,'importar_rodada', 'importar_dados_pessoas', 'importar_jogos_live']
    
    def importar_jogos(self, request, queryset):
        """
        Função que importa todos jogos
        """
        camp_fonte = ''
        for campeonato in queryset:
            fonte_camp = SourceCampeonato.objects.filter(id_campeonato=campeonato.id_campeonato)
            if not fonte_camp:
                if camp_fonte:
                    camp_fonte += ', '
                camp_fonte += normalize('NFKD', campeonato.nome).encode('ASCII', 'ignore')
        if camp_fonte:
            message_bit = "Os campeonatos %s não possuem relação fonte"%(camp_fonte)
            self.message_user(request, "%s ." % message_bit)
        else:
            lista_campeonatos = []
            for campeonato in queryset:
                fonte_camp = SourceCampeonato.objects.filter(id_campeonato=campeonato.id_campeonato)[0]
                lista_campeonatos.append(fonte_camp)
            importar_jogos(lista_campeonatos=lista_campeonatos, tipo_busca='season')
            message_bit = "Os campeonatos foram atualizados com sucesso"
            self.message_user(request, "%s ." % message_bit)

    importar_jogos.short_description = 'Importar/Atualizar jogos(por campeonato selecionado)'
    
    def importar_pessoas(self, request, queryset):
        """
        Função que importa todas pessoas
        """
        camp_fonte = ''
        for campeonato in queryset:
            fonte_camp = SourceCampeonato.objects.filter(id_campeonato=campeonato.id_campeonato)
            if not fonte_camp:
                if camp_fonte:
                    camp_fonte += ', '
                camp_fonte += normalize('NFKD', campeonato.nome).encode('ASCII', 'ignore')
        if camp_fonte:
            message_bit = "Os campeonatos %s não possuem relação fonte"%(camp_fonte)
            self.message_user(request, "%s ." % message_bit)
        else:
            lista_campeonatos = []
            for campeonato in queryset:
                fonte_camp = SourceCampeonato.objects.filter(id_campeonato=campeonato.id_campeonato)[0]
                lista_campeonatos.append(fonte_camp)
            importar_pessoas(lista_campeonatos=lista_campeonatos, tipo_busca='season')
            message_bit = "As pessoas foram importadas com sucesso"
            self.message_user(request, "%s ." % message_bit)

    importar_pessoas.short_description = 'Importar/Atualizar pessoas(por campeonato selecionado)'
    
    def importar_rodada(self, request, queryset):
        """
        Função que importa jogos por rodada
        """
        importar_rodada()
        message_bit = "Os jogos foram importadas com sucesso"
        self.message_user(request, "%s ." % message_bit)

    importar_rodada.short_description = 'Importar rodada(rotina)'
    
    def importar_jogos_live(self, request, queryset):
        """
        Função que importa jogos por rodada
        """
        importar_jogos_live()
        message_bit = "Os jogos foram importadas com sucesso"
        self.message_user(request, "%s ." % message_bit)

    importar_jogos_live.short_description = 'Importar jogos live(rotina)'
    
    def importar_dados_pessoas(self, request, queryset):
        """
        Função que importa dados de pessoas
        """
        importar_dados_pessoas()
        message_bit = "Os dados foram importadas com sucesso"
        self.message_user(request, "%s ." % message_bit)

    importar_dados_pessoas.short_description = 'Importar dados pessoas(rotina)'
    
class SourceCampeonatoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Campeonato'
        
    search_fields = ('id_campeonato__nome', )
    ordering = ['id_campeonato', 'id_source_campeonato']
    list_display = ('id_source_campeonato', 'id_campeonato', 'value', 'tipo', )
    raw_id_fields = ('id_campeonato', )

class CampeonatoFaseTipoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Campeonato Fase Tipo'
        
    search_fields = ('nome', 'id_pais__nome_pt', 'id_estado__nome')
    ordering = ['id_pais', 'id_estado', 'id_campeonato_fase_tipo']
    list_display = ('id_campeonato_fase_tipo', 'nome', 'id_continente', 'id_pais', 'id_estado', 'slug', )
    raw_id_fields = ('id_estado', 'id_pais', 'id_continente' )
    
    
class CampeonatoFaseGrupoInline(admin.TabularInline):
    model = CampeonatoFaseGrupo

class CampeonatoFaseAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Campeonato Fase'
        
    search_fields = ('id_campeonato__nome', )
    ordering = ['id_campeonato', 'id_campeonato_fase']
    list_display = ('id_campeonato_fase', 'nome', 'id_campeonato_fase_tipo', 'id_campeonato', 'data_inicio', 'data_fim', 'slug', 'ativo_set', 'rodada_atualizacao', )
    raw_id_fields = ('id_campeonato', 'id_campeonato_fase_tipo', )
    inlines = [
        CampeonatoFaseGrupoInline,
    ]

class SourceCampeonatoFaseAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Campeonato Fase'
        
    search_fields = ('id_campeonato_fase__nome', )
    ordering = ['id_campeonato_fase', 'id_source_campeonato_fase']
    list_display = ('id_source_campeonato_fase', 'id_campeonato_fase', 'value', 'tipo', 'tipo_rodada_set', )
    raw_id_fields = ('id_campeonato_fase', )
    
class CampeonatoFaseGrupoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Campeonato Fase Grupo'
        
    search_fields = ('id_campeonato_fase__nome', )
    ordering = ['id_campeonato_fase', 'id_campeonato_fase_grupo']
    list_display = ('id_campeonato_fase_grupo', 'nome', 'id_campeonato_fase', 'qtd_rodadas', 'slug', )
    raw_id_fields = ('id_campeonato_fase', )
    
class CampeonatoFaseGrupoTabelaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Campeonato Fase Grupo Tabela'
        
    search_fields = ('id_campeonato_fase__nome', 'id_campeonato_fase_grupo__nome')
    ordering = ['id_campeonato_fase_grupo_tabela']
    list_display = ('id_campeonato_fase_grupo_tabela', 'id_campeonato_fase', 'id_campeonato_fase_grupo', 'id_time', 'pontos', 
                    'jogos', 'vitorias', 'empates', 'derrotas', 'gols_pro', 'cartoes_amarelos', 'cartoes_vermelhos', )
    raw_id_fields = ('id_campeonato_fase', 'id_campeonato_fase_grupo', 'id_time')
    
    

admin.site.register(Temporada, TemporadaAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(SourceCampeonato, SourceCampeonatoAdmin)
admin.site.register(CampeonatoFaseTipo, CampeonatoFaseTipoAdmin)
admin.site.register(CampeonatoFase, CampeonatoFaseAdmin)
admin.site.register(SourceCampeonatoFase, SourceCampeonatoFaseAdmin)
admin.site.register(CampeonatoFaseGrupo, CampeonatoFaseGrupoAdmin)
admin.site.register(CampeonatoFaseGrupoTabela, CampeonatoFaseGrupoTabelaAdmin)