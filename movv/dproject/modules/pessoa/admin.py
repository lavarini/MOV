# -*- encoding: utf-8 -*-
################################################################################
# Administração do módulo localizacao
#
# @author: Alexandre Lavarini Matoso
# @since: 04/05/2011
################################################################################

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from futebol.modules.pessoa.models import Pessoa, SourcePessoa,\
     Funcao, PessoaFuncao, PessoaNacionalidade, FotoPessoa
from crawler_futebol.views import importar_dados_pessoas

from unicodedata import normalize

class PessoaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Pessoa'
        
    search_fields = ('nome_completo', 'nome_popular')
    ordering = ['id_pessoa']
    list_display = ('id_pessoa', 'id_cidade', 'nome_completo', 'nome_popular', 'status', 'data_atualizacao')
    raw_id_fields = ('id_cidade', )
    
    actions = ['importar_dados_pessoas']
    
    def importar_dados_pessoas(self, request, queryset):
        """
        Função que importa dados das pessoas
        """
        pessoa_fonte = ''
        for pessoa in queryset:
            fonte_pessoa = SourcePessoa.objects.filter(id_pessoa=pessoa.id_pessoa)
            if not fonte_pessoa:
                if pessoa_fonte:
                    pessoa_fonte += ', '
                pessoa_fonte += normalize('NFKD', pessoa.nome_completo).encode('ASCII', 'ignore')
        if pessoa_fonte:
            message_bit = "As pessoas %s não possuem relação fonte"%(pessoa_fonte)
            self.message_user(request, "%s ." % message_bit)
        else:
            lista_pessoas = []
            for pessoa in queryset:
                fonte_pessoa = SourcePessoa.objects.get(id_pessoa=pessoa.id_pessoa)
                lista_pessoas.append(fonte_pessoa)
            importar_dados_pessoas(lista_pessoas=lista_pessoas, tipo_busca='player')
            message_bit = "As pessoas foram atualizados com sucesso"
            self.message_user(request, "%s ." % message_bit)

    importar_dados_pessoas.short_description = 'Importar/Atualizar dados das pessoas'

class SourcePessoaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Source Pessoa'
        
    search_fields = ('id_pessoa__nome_completo', 'id_pessoa__nome_popular', )
    ordering = ['id_pessoa']
    list_display = ('id_source_pessoa', 'id_pessoa', 'value', 'tipo',)
    raw_id_fields = ('id_pessoa', )
    
class FuncaoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Funcao'
        
    search_fields = ('nome', )
    ordering = ['id_funcao']
    list_display = ('id_funcao', 'nome', 'slug', )

class PessoaFuncaoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Pessoa Funcao'
        
    search_fields = ('id_pessoa__nome_completo', 'id_pessoa__nome_popular', 'id_funcao__nome')
    ordering = ['id_pessoa']
    list_display = ('id_pessoa_funcao', 'id_funcao', 'id_pessoa', )
    raw_id_fields = ('id_pessoa',)

class PessoaNacionalidadeAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Pessoa Funcao'
        
    search_fields = ('id_pessoa__nome_completo', 'id_pessoa__nome_popular', 'id_pais__nome_pt')
    ordering = ['id_pessoa']
    list_display = ('id_pessoa_nacionalidade', 'id_pessoa', 'id_pais', 'nativo', )
    raw_id_fields = ('id_pessoa', 'id_pais')

class FotoPessoaAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Foto Pessoa'
        
    search_fields = ('id_pessoa__nome_completo', 'id_pessoa__nome_popular', )
    ordering = ['id_pessoa']
    list_display = ('id_foto_pessoa', 'id_pessoa', 'url', 'data_insercao', )
    raw_id_fields = ('id_pessoa', )
    
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(SourcePessoa, SourcePessoaAdmin)
admin.site.register(Funcao, FuncaoAdmin)
admin.site.register(PessoaFuncao, PessoaFuncaoAdmin)
admin.site.register(PessoaNacionalidade, PessoaNacionalidadeAdmin)
admin.site.register(FotoPessoa, FotoPessoaAdmin)