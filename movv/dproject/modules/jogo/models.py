# -*- coding: utf-8 -*-
###############################################################################
# Modulo de gerenciamento
#
# @author: Alexandre Lavarini Matoso
# @since: 04/05/2011
###############################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _
from futebol.modules.time.models import Time
from futebol.modules.campeonato.models import Campeonato,\
     CampeonatoFase, CampeonatoFaseGrupo
from futebol.modules.pessoa.models import PessoaFuncao
from futebol.modules.estadio.models import Estadio
import datetime

TIMES_CHOICES = (
    ('clube', 'clube'),
    ('selecao', 'selecao'),
)

SOURCE_CHOICES = (
    ('terra', 'terra'),
    ('globo', 'globo'),
    ('uol', 'uol'),
    ('gsm', 'gsm'),
)

class Escalacao(models.Model):
    id_escalacao = models.AutoField(primary_key=True, serialize=True)
    formacao_tatica = models.CharField(max_length=10)
    id_time = models.ForeignKey(Time,
                                related_name='id_time_escalacao',
                                db_column='id_time')
    
    class Meta:
        verbose_name = ('Escalação')
        verbose_name_plural = ('Escalações')
        db_table = u'escalacao'
        
    def __unicode__(self):
        return self.formacao_tatica

class EscalacaoPessoaFuncao(models.Model):
    id_escalacao_pessoa_funcao = models.AutoField(primary_key=True, serialize=True)
    id_escalacao = models.ForeignKey(Escalacao,
                                     related_name='id_escalacao_formacao',
                                     db_column='id_escalacao')
    id_pessoa_funcao = models.ForeignKey(PessoaFuncao,
                                         related_name='id_pessoa_funcao_escalacao',
                                         db_column='id_pessoa_funcao')
    titular = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Escalacao Pessoa Funcao')
        verbose_name_plural = ('Escalações Pessoas Função')
        db_table = u'escalacao_pessoa_funcao'
        
    def __unicode__(self):
        return str(self.id_escalacao_pessoa_funcao)
        
class SourceEscalacaoPessoaFuncao(models.Model):
    id_source_escalacao_pessoa_funcao = models.AutoField(primary_key=True, serialize=True)
    id_escalacao_pessoa_funcao = models.ForeignKey(EscalacaoPessoaFuncao,
                                                   related_name='id_escalacao_pessoa_funcao_source',
                                                   db_column='id_escalacao_pessoa_funcao')
    tipo = models.CharField(_('Tipo'),
                             choices=SOURCE_CHOICES,
                             max_length=10,
                             help_text='Tipo do source')

    value = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ('Source Escalacao Pessoa Funcao')
        verbose_name_plural = ('Source Escalações Pessoas Função')
        db_table = u'source_escalacao_pessoa_funcao'
        
    def __unicode__(self):
        return self.value

class JogoTipo(models.Model):
    id_jogo_tipo = models.AutoField(primary_key=True, serialize=True)
    nome = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ('Jogo Tipo')
        verbose_name_plural = ('Jogo Tipos')
        db_table = u'jogo_tipo'
        
    def __unicode__(self):
        return self.nome

class Jogo(models.Model):
    id_jogo = models.AutoField(primary_key=True, serialize=True)
    
    id_jogo_tipo = models.ForeignKey(JogoTipo,
                                     related_name='id_jogo_tipo_jogo',
                                     db_column='id_jogo_tipo')
    id_time_mandante = models.ForeignKey(Time,
                                         related_name='id_time_mandante',
                                         db_column='id_time_mandante')
    id_time_visitante = models.ForeignKey(Time,
                                          related_name='id_time_visitante',
                                          db_column='id_time_visitante')
    id_campeonato = models.ForeignKey(Campeonato,
                                      related_name='id_campeonato_jogo',
                                      db_column='id_campeonato')
    id_campeonato_fase = models.ForeignKey(CampeonatoFase,
                                           related_name='id_campeonato_fase_jogo',
                                           db_column='id_campeonato_fase')
    id_campeonato_fase_grupo = models.ForeignKey(CampeonatoFaseGrupo,
                                                 related_name='id_campeonato_fase_grupo_jogo',
                                                 db_column='id_campeonato_fase_grupo')
    id_escalacao_mandante = models.ForeignKey(Escalacao,
                                              related_name='id_escalacao_mandante_jogo',
                                              db_column='id_escalacao_mandante',
                                              null=True, blank=True)
    id_escalacao_visitante = models.ForeignKey(Escalacao,
                                               related_name='id_escalacao_visitante_jogo',
                                               db_column='id_escalacao_visitante',
                                               null=True, blank=True)
    id_escalacao_arbitragem = models.ForeignKey(Escalacao,
                                                related_name='id_escalacao_arbitragem_jogo',
                                                db_column='id_escalacao_arbitragem',
                                                null=True, blank=True)
    id_estadio = models.ForeignKey(Estadio,
                                   related_name='id_estadio_jogo',
                                   db_column='id_estadio',
                                   null=True, blank=True)
    rodada = models.SmallIntegerField()
    data_insercao = models.DateTimeField(default=datetime.datetime.now)
    data = models.DateTimeField(null=True, blank=True)
    data_ultima_atualizacao = models.DateTimeField(null=True, blank=True)
    placar_time_mandante = models.SmallIntegerField(null=True, blank=True)
    placar_time_visitante = models.SmallIntegerField(null=True, blank=True)
    placar_penaltis_mandante = models.SmallIntegerField(null=True, blank=True)
    placar_penaltis_visitante = models.SmallIntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = ('Jogo')
        verbose_name_plural = ('Jogos')
        db_table = u'jogo'
        
    def __unicode__(self):
        return str(self.id_jogo)
        
class SourceJogo(models.Model):
    id_source_jogo = models.AutoField(primary_key=True, serialize=True)
    id_jogo = models.ForeignKey(Jogo,
                                related_name='id_jogo_source',
                                db_column='id_jogo')
    tipo = models.CharField(_('Tipo'),
                             choices=SOURCE_CHOICES,
                             max_length=10,
                             help_text='Tipo do source')

    value = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ('Source Jogo')
        verbose_name_plural = ('Source Jogos')
        db_table = u'source_jogo'
        
    def __unicode__(self):
        return self.value
        
class EventoCategoria(models.Model):
    id_evento_categoria = models.AutoField(primary_key=True, serialize=True)
    nome = models.CharField(max_length=45)
    
    class Meta:
        verbose_name = ('Evento Categoria')
        verbose_name_plural = ('Evento Categorias')
        db_table = u'evento_categoria'
        
    def __unicode__(self):
        return self.nome
    
class EventoJogo(models.Model):
    id_evento_jogo = models.AutoField(primary_key=True, serialize=True)
    id_evento_categoria = models.ForeignKey(EventoCategoria,
                                            related_name='id_evento_categoria_jogo',
                                            db_column='id_evento_categoria')
    id_jogo = models.ForeignKey(Jogo,
                                related_name='id_jogo_evento_jogo',
                                db_column='id_jogo')
    id_time = models.ForeignKey(Time,
                                related_name='id_time_evento_jogo',
                                db_column='id_time')
    id_pessoa_funcao = models.ForeignKey(PessoaFuncao,
                                         related_name='id_pessoa_funcao_jogo',
                                         db_column='id_pessoa_funcao')
    
    momento = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Evento Jogo')
        verbose_name_plural = ('Eventos Jogo')
        db_table = u'evento_jogo'
        
    def __unicode__(self):
        return str(self.id_evento_jogo)
        
class SourceEventoJogo(models.Model):
    id_source_evento_jogo = models.AutoField(primary_key=True, serialize=True)
    id_evento_jogo = models.ForeignKey(EventoJogo,
                                       related_name='id_evento_jogo_source',
                                       db_column='id_evento_jogo')
    tipo = models.CharField(_('Tipo'),
                             choices=SOURCE_CHOICES,
                             max_length=10,
                             help_text='Tipo do source')

    value = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ('Source Evento Jogo')
        verbose_name_plural = ('Source Eventos Jogo')
        db_table = u'source_evento_jogo'
        
    def __unicode__(self):
        return self.value
    
class JogoSubstituicao(models.Model):
    id_jogo_substituicao = models.AutoField(primary_key=True, serialize=True)
    
    id_jogo = models.ForeignKey(Jogo,
                                related_name='id_jogo_substituicao',
                                db_column='id_jogo')
    id_pessoa_funcao_de = models.ForeignKey(PessoaFuncao,
                                            related_name='id_pessoa_funcao_de',
                                            db_column='id_pessoa_funcao_de')
    id_pessoa_funcao_por = models.ForeignKey(PessoaFuncao,
                                             related_name='id_pessoa_funcao_por',
                                             db_column='id_pessoa_funcao_por')
    id_time = models.ForeignKey(Time,
                                related_name='id_time_jogo_substituicao',
                                db_column='id_time')
    momento = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Jogo Substituicao')
        verbose_name_plural = ('Jogo Substituicoes')
        db_table = u'jogo_substituicao'
        
    def __unicode__(self):
        return str(self.id_substituicao)
        
class SourceJogoSubstituicao(models.Model):
    id_source_jogo_substituicao = models.AutoField(primary_key=True, serialize=True)
    id_jogo_substituicao = models.ForeignKey(JogoSubstituicao,
                                             related_name='id_jogo_substituicao_source',
                                             db_column='id_jogo_substituicao')
    tipo = models.CharField(_('Tipo'),
                             choices=SOURCE_CHOICES,
                             max_length=10,
                             help_text='Tipo do source')

    value = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ('Source Jogo Substituicao')
        verbose_name_plural = ('Source Jogo Substituicoes')
        db_table = u'source_jogo_substituicao'
        
    def __unicode__(self):
        return self.value
    
class JogoView(models.Model):
    id_jogo = models.AutoField(primary_key=True, serialize=True)
    
    id_jogo_tipo = models.ForeignKey(JogoTipo,
                                     related_name='id_jogo_tipo_jogo_view',
                                     db_column='id_jogo_tipo')
    id_time_mandante = models.ForeignKey(Time,
                                         related_name='id_time_mandante_view',
                                         db_column='id_time_mandante')
    id_time_visitante = models.ForeignKey(Time,
                                          related_name='id_time_visitante_view',
                                          db_column='id_time_visitante')
    id_campeonato_fase = models.ForeignKey(CampeonatoFase,
                                           related_name='id_campeonato_fase_jogo_view',
                                           db_column='id_campeonato_fase')
    id_estadio = models.ForeignKey(Estadio,
                                   related_name='id_estadio_jogo_views',
                                   db_column='id_estadio',
                                   null=True, blank=True)
    id_escalacao_mandante = models.ForeignKey(Escalacao,
                                              related_name='id_escalacao_mandante_jogo_view',
                                              db_column='id_escalacao_mandante',
                                              null=True, blank=True)
    id_escalacao_visitante = models.ForeignKey(Escalacao,
                                               related_name='id_escalacao_visitante_jogo_view',
                                               db_column='id_escalacao_visitante',
                                               null=True, blank=True)
    rodada = models.SmallIntegerField()
    data_insercao = models.DateTimeField(default=datetime.datetime.now)
    data = models.DateTimeField(null=True, blank=True)
    data_ultima_atualizacao = models.DateTimeField(null=True, blank=True)
    placar_time_mandante = models.SmallIntegerField(null=True, blank=True)
    placar_time_visitante = models.SmallIntegerField(null=True, blank=True)
    placar_penaltis_mandante = models.SmallIntegerField(null=True, blank=True)
    placar_penaltis_visitante = models.SmallIntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = ('View Jogo')
        verbose_name_plural = ('View Jogos')
        db_table = u'jogo'
        
    def __unicode__(self):
        return str(self.id_jogo)
    
class EventoJogoView(models.Model):
    id_evento_jogo = models.AutoField(primary_key=True, serialize=True)
    id_evento_categoria = models.ForeignKey(EventoCategoria,
                                            related_name='id_evento_categoria_jogo_view',
                                            db_column='id_evento_categoria')
    id_jogo = models.SmallIntegerField()
    id_time = models.ForeignKey(Time,
                                related_name='id_time_evento_jogo_view',
                                db_column='id_time')
    id_pessoa_funcao = models.ForeignKey(PessoaFuncao,
                                         related_name='id_pessoa_funcao_jogo_view',
                                         db_column='id_pessoa_funcao')
    momento = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('View Evento Jogo')
        verbose_name_plural = ('View Eventos Jogo')
        db_table = u'evento_jogo'
        
    def __unicode__(self):
        return str(self.id_evento_jogo)
    
class JogoSubstituicaoView(models.Model):
    id_jogo_substituicao = models.AutoField(primary_key=True, serialize=True)
    
    id_jogo = models.SmallIntegerField()
    
    id_pessoa_funcao_de = models.ForeignKey(PessoaFuncao,
                                            related_name='id_pessoa_funcao_de_view',
                                            db_column='id_pessoa_funcao_de')
    id_pessoa_funcao_por = models.ForeignKey(PessoaFuncao,
                                             related_name='id_pessoa_funcao_por_view',
                                             db_column='id_pessoa_funcao_por')
    momento = models.SmallIntegerField()
    
    id_time = models.ForeignKey(Time,
                                related_name='id_time_jogo_substituicao_view',
                                db_column='id_time')
    
    class Meta:
        verbose_name = ('View Jogo Substituicao')
        verbose_name_plural = ('View Jogo Substituicoes')
        db_table = u'jogo_substituicao'
        
    def __unicode__(self):
        return str(self.id_substituicao)