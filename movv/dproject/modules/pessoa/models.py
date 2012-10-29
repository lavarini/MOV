# -*- coding: utf-8 -*-
###############################################################################
# Modulo de gerenciamento
#
# @author: Alexandre Lavarini Matoso
# @since: 04/05/2011
###############################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _
from futebol.modules.localizacao.models import Cidade, Pais
import datetime

STATUS_CHOICES = (
    ('em_atividade', 'em_atividade'),
    ('aposentado', 'aposentado'),
    ('falecido', 'falecido'),
)

SOURCE_CHOICES = (
    ('terra', 'terra'),
    ('globo', 'globo'),
    ('uol', 'uol'),
    ('gsm', 'gsm'),
)

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True, serialize=True)
    id_cidade = models.ForeignKey(Cidade,
                                  related_name='id_cidade_pessoa',
                                  db_column='id_cidade')
    nome_completo = models.CharField(max_length=100)
    nome_popular = models.CharField(max_length=100)
    status = models.CharField(_('Status'),
                             choices=STATUS_CHOICES,
                             max_length=20,
                             help_text='Status pessoa')
    data_nascimento = models.DateField(null=True, blank=True)
    data_obito = models.DateField(null=True, blank=True)
    pe_preferencial = models.CharField(max_length=45,
                                       null=True, blank=True)
    altura = models.CharField(max_length=45,
                              null=True, blank=True)
    peso = models.CharField(max_length=45,
                            null=True, blank=True)
    site_oficial = models.CharField(max_length=45,
                                    null=True, blank=True)
    twitter = models.CharField(max_length=100,
                               null=True, blank=True)
    facebook = models.CharField(max_length=200,
                                null=True, blank=True)
    orkut = models.CharField(max_length=200,
                             null=True, blank=True)
    data_atualizacao = models.CharField(max_length=45,
                                    null=True, blank=True)
    
    class Meta:
        verbose_name = ('Pessoa')
        verbose_name_plural = ('Pessoas')
        db_table = u'pessoa'
    
    def __unicode__(self):
        return self.nome_popular
    
class SourcePessoa(models.Model):
    id_source_pessoa = models.AutoField(primary_key=True, serialize=True)
    id_pessoa = models.ForeignKey(Pessoa,
                                  related_name='id_pessoa_source',
                                  db_column='id_pessoa')
    tipo = models.CharField(_('Tipo'),
                             choices=SOURCE_CHOICES,
                             max_length=10,
                             help_text='Tipo do source')

    value = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ('Source Pessoa')
        verbose_name_plural = ('Source Pessoa')
        db_table = u'source_pessoa'
        
    def __unicode__(self):
        return self.value   

class Funcao(models.Model):
    id_funcao = models.AutoField(primary_key=True, serialize=True)
    nome = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ('Funcao')
        verbose_name_plural = ('Funcoes')
        db_table = u'funcao'
        
    def __unicode__(self):
        return self.nome
    
class PessoaFuncao(models.Model):
    id_pessoa_funcao = models.AutoField(primary_key=True, serialize=True)
    id_funcao = models.ForeignKey(Funcao,
                                      related_name='id_funcao_pessoa',
                                      db_column='id_funcao')
    id_pessoa = models.ForeignKey(Pessoa,
                                  related_name='id_pessoa_funcao',
                                  db_column='id_pessoa')
    
    class Meta:
        verbose_name = ('Pessoa Funcao')
        verbose_name_plural = ('Pessoa Funcoes')
        db_table = u'pessoa_funcao'
    
    def __unicode__(self):
        return self.id_pessoa.nome_popular + ' (' + self.id_funcao.nome + ')'
    
class PessoaNacionalidade(models.Model):
    id_pessoa_nacionalidade = models.AutoField(primary_key=True, serialize=True)
    id_pessoa = models.ForeignKey(Pessoa,
                                  related_name='id_pessoa_pais',
                                  db_column='id_pessoa')
    id_pais = models.ForeignKey(Pais,
                                related_name='id_pais_pessoa',
                                db_column='id_pais')
    nativo = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Pessoa Nacionalidade')
        verbose_name_plural = ('Pessoas Nacionalidade')
        db_table = u'pessoa_nacionalidade'
    
    def __unicode__(self):
        return self.id_pessoa.nome_popular + ' (' + self.id_pais.nome_pt + ')'
    
class FotoPessoa(models.Model):
    id_foto_pessoa = models.AutoField(primary_key=True, serialize=True)
    id_pessoa = models.ForeignKey(Pessoa,
                                  related_name='id_pessoa_foto',
                                  db_column='id_pessoa')
    url = models.CharField(max_length=45)
    data_insercao = models.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        verbose_name = ('Foto Pessoa')
        verbose_name_plural = ('Fotos Pessoas')
        db_table = u'foto_pessoa'
    
    def __unicode__(self):
        return self.url