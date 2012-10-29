# -*- encoding: utf-8 -*-
################################################################################
# Administração do módulo localizacao
#
# @author: Alexandre Lavarini Matoso
# @since: 04/05/2011
################################################################################

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from futebol.modules.jogo.models import Jogo, Escalacao,\
     JogoTipo, SourceJogo, EventoCategoria, EventoJogo,\
     JogoSubstituicao, JogoView, EventoJogoView, JogoSubstituicaoView,\
     SourceEventoJogo, SourceJogoSubstituicao, EscalacaoPessoaFuncao
from crawler_futebol.views import importar_dados_jogos

from unicodedata import normalize

class EscalacaoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Escalacao'
        
    search_fields = ('formacao_tatica', 'id_escalacao')
    ordering = ['id_escalacao']
    list_display = ('id_escalacao', 'formacao_tatica', 'id_time')

class EscalacaoPessoaFuncaoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Escalacao Pessoa Funcao'
        
    search_fields = ('formacao_tatica', 'id_escalacao')
    ordering = ['id_escalacao', 'id_escalacao_pessoa_funcao']
    list_display = ('id_escalacao_pessoa_funcao', 'id_escalacao', 'id_pessoa_funcao', 'titular', )
    
class JogoTipoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Jogo Tipo'
        
    search_fields = ('nome', 'id_jogo_tipo')
    ordering = ['id_jogo_tipo']
    list_display = ('id_jogo_tipo', 'nome', 'slug', )
    
class JogoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Jogo'
        
    search_fields = ('id_campeonato_fase__nome', 'id_jogo')
    ordering = ['id_jogo']
    list_display = ('id_jogo', )
    
    raw_id_fields = ('id_campeonato_fase', 'id_campeonato_fase_grupo')
    
    actions = ['importar_dados_jogos']
    
    def importar_dados_jogos(self, request, queryset):
        """
        Função que importa dados dos jogos
        """
        jogo_fonte = ''
        for jogo in queryset:
            fonte_jogo = SourceJogo.objects.filter(id_jogo=jogo.id_jogo)
            if not fonte_jogo:
                if jogo_fonte:
                    jogo_fonte += ', '
                jogo_fonte += normalize('NFKD', jogo.id_jogo).encode('ASCII', 'ignore')
        if jogo_fonte:
            message_bit = "Os jogos %s não possuem relação fonte"%(jogo_fonte)
            self.message_user(request, "%s ." % message_bit)
        else:
            lista_jogos = []
            for jogo in queryset:
                fonte_jogo = SourceJogo.objects.get(id_jogo=jogo.id_jogo)
                lista_jogos.append(fonte_jogo)
            importar_dados_jogos(lista_jogos=lista_jogos, tipo_busca='match')
            message_bit = "Os jogos foram atualizados com sucesso"
            self.message_user(request, "%s ." % message_bit)

    importar_dados_jogos.short_description = 'Importar/Atualizar dados dos jogos'
    
class SourceJogoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Jogo'
        
    ordering = ['id_source_jogo']
    list_display = ('id_source_jogo', 'value', 'tipo', )
    raw_id_fields = ('id_jogo', )
    
class EventoCategoriaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Evento Categoria'
        
    search_fields = ('nome',)
    ordering = ['id_evento_categoria']
    list_display = ('id_evento_categoria', 'nome',)

class EventoJogoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Evento Jogo'
        
    ordering = ['id_jogo']
    list_filter = ('id_evento_categoria',)
    list_display = ('id_evento_jogo',)
    
    raw_id_fields = ('id_jogo', 'id_time', 'id_pessoa_funcao')
    
class SourceEventoJogoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Evento Jogo'
        
    ordering = ['id_evento_jogo', 'id_source_evento_jogo']
    list_display = ('id_source_evento_jogo', 'value', 'tipo', )
    raw_id_fields = ('id_evento_jogo', )
    
class JogoSubstituicaoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Jogo Substituicao'
        
    ordering = ['id_jogo_substituicao']
    list_display = ('id_jogo_substituicao',)
    
    raw_id_fields = ('id_jogo', 'id_pessoa_funcao_de', 'id_pessoa_funcao_por')
    
class SourceJogoSubstituicaoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Evento Jogo'
        
    ordering = ['id_jogo_substituicao', 'id_source_jogo_substituicao']
    list_display = ('id_source_jogo_substituicao', 'value', 'tipo', )
    raw_id_fields = ('id_jogo_substituicao', )
    
    
class JogoViewAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'View Jogo'
        
    search_fields = ('id_campeonato_fase__nome', 'rodada')
    ordering = ['id_jogo']
    list_display = ('id_jogo', 'id_campeonato_fase', 'id_escalacao_mandante', 'id_time_mandante', 'placar_time_mandante',\
                    'id_escalacao_visitante', 'id_time_visitante', 'placar_time_visitante', 'data', 'rodada', 'id_estadio')
    
    raw_id_fields = ('id_campeonato_fase',)
    
class EventoJogoViewAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'View Evento Jogo'
        
    search_fields = ('id_evento_categoria__nome', 'id_time__nome_popular', 'id_time__nome_completo')
    ordering = ['id_jogo']
    list_filter = ('id_evento_categoria',)
    list_display = ('id_evento_jogo', 'id_jogo', 'id_time', 'id_pessoa_funcao', 'id_evento_categoria', 'momento',)
    
    raw_id_fields = ('id_time', )
    
class JogoSubstituicaoViewAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'View Jogo Substituicao'
        
    ordering = ['id_jogo_substituicao']
    list_display = ('id_jogo_substituicao', 'id_jogo', 'id_time', 'id_pessoa_funcao_de', 'id_pessoa_funcao_por')


admin.site.register(Escalacao, EscalacaoAdmin)
admin.site.register(EscalacaoPessoaFuncao, EscalacaoPessoaFuncaoAdmin)
admin.site.register(JogoTipo, JogoTipoAdmin)
admin.site.register(Jogo, JogoAdmin)
admin.site.register(SourceJogo, SourceJogoAdmin)
admin.site.register(EventoCategoria, EventoCategoriaAdmin) 
admin.site.register(EventoJogo, EventoJogoAdmin)
admin.site.register(SourceEventoJogo, SourceEventoJogoAdmin)
admin.site.register(JogoSubstituicao, JogoSubstituicaoAdmin)
admin.site.register(SourceJogoSubstituicao, SourceJogoSubstituicaoAdmin)
admin.site.register(JogoView, JogoViewAdmin)
admin.site.register(EventoJogoView, EventoJogoViewAdmin)
admin.site.register(JogoSubstituicaoView, JogoSubstituicaoViewAdmin)