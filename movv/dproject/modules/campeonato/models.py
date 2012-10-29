# -*- coding: utf-8 -*-
###############################################################################
# Modulo de gerenciamento
#
# @author: Alexandre Lavarini Matoso
# @since: 04/05/2011
###############################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _
from futebol.modules.localizacao.models import Continente, Estado, Pais
from futebol.modules.time.models import Time


SOURCE_CHOICES = (
    ('terra', 'terra'),
    ('globo', 'globo'),
    ('uol', 'uol'),
    ('gsm', 'gsm'),
)

class Temporada(models.Model):
    id_temporada = models.AutoField(primary_key=True, serialize=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    
    class Meta:
        verbose_name = ('Temporada')
        verbose_name_plural = ('Temporadas')
        db_table = u'temporada'
        
    def __unicode__(self):
        return str(self.data_inicio)

class Campeonato(models.Model):
    id_campeonato = models.AutoField(primary_key=True, serialize=True)
    id_temporada = models.ForeignKey(Temporada,
                                     related_name='id_temporada_campeonato',
                                     db_column='id_temporada')
    
    nome = models.CharField(max_length=60)
    slug = models.CharField(max_length=70)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True, blank=True)
    ativo_set = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Campeonato')
        verbose_name_plural = ('Campeonatos')
        db_table = u'campeonato'
        
    def __unicode__(self):
        return self.nome
    
class SourceCampeonato(models.Model):
    id_source_campeonato = models.AutoField(primary_key=True, serialize=True)
    id_campeonato = models.ForeignKey(Campeonato,
                                      related_name='id_campeonato_source',
                                      db_column='id_campeonato')
    tipo = models.CharField(_('Tipo'),
                             choices=SOURCE_CHOICES,
                             max_length=10,
                             help_text='Tipo do source')

    value = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ('Source Campeonato')
        verbose_name_plural = ('Source Campeonatos')
        db_table = u'source_campeonato'
        
    def __unicode__(self):
        return self.value
    
class CampeonatoFaseTipo(models.Model):
    id_campeonato_fase_tipo = models.AutoField(primary_key=True, serialize=True)
    id_continente = models.ForeignKey(Continente,
                                      related_name='id_continente_campeonato_fase_tipo',
                                      db_column='id_continente',
                                      null=True, blank=True)
    id_pais = models.ForeignKey(Pais,
                                related_name='id_pais_campeonato_fase_tipo',
                                db_column='id_pais',
                                null=True, blank=True)
    id_estado = models.ForeignKey(Estado,
                                  related_name='id_estado_campeonato_fase_tipo',
                                  db_column='id_estado',
                                  null=True, blank=True)
    
    prioridade_set = models.SmallIntegerField()
    nome = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ('Campeonato Fase Tipo')
        verbose_name_plural = ('Campeonato Fase Tipos')
        db_table = u'campeonato_fase_tipo'
        
    def __unicode__(self):
        return self.nome
    
class CampeonatoFase(models.Model):
    id_campeonato_fase = models.AutoField(primary_key=True, serialize=True)
    id_campeonato = models.ForeignKey(Campeonato,
                                      related_name='id_campeonato_campeonato_fase',
                                      db_column='id_campeonato')
    id_campeonato_fase_tipo = models.ForeignKey(CampeonatoFaseTipo,
                                                related_name='id_campeonato_fase_tipo_campeonato_fase',
                                                db_column='id_campeonato_fase_tipo')
    
    nome = models.CharField(max_length=60)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True, blank=True)
    config_cores = models.CharField(max_length=300, null=True, blank=True)
    ativo_set = models.SmallIntegerField()
    slug = models.CharField(max_length=70)
    rodada_atualizacao = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Campeonato Fase')
        verbose_name_plural = ('Campeonato Fases')
        db_table = u'campeonato_fase'
        
    def __unicode__(self):
        return self.nome
    
class SourceCampeonatoFase(models.Model):
    id_source_campeonato_fase = models.AutoField(primary_key=True, serialize=True)
    id_campeonato_fase = models.ForeignKey(CampeonatoFase,
                                           related_name='id_campeonato_fase_source',
                                           db_column='id_campeonato_fase')
    tipo = models.CharField(_('Tipo'),
                             choices=SOURCE_CHOICES,
                             max_length=10,
                             help_text='Tipo do source')

    value = models.CharField(max_length=200)
    tipo_rodada_set = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Source Campeonato Fase')
        verbose_name_plural = ('Source Campeonato Fases')
        db_table = u'source_campeonato_fase'
        
    def __unicode__(self):
        return self.value
        
class CampeonatoFaseGrupo(models.Model):
    id_campeonato_fase_grupo = models.AutoField(primary_key=True, serialize=True)
    id_campeonato_fase = models.ForeignKey(CampeonatoFase,
                                           related_name='id_campeonato_fase_fase_grupo',
                                           db_column='id_campeonato_fase')
     
    
    nome = models.CharField(max_length=40)
    qtd_rodadas = models.SmallIntegerField()
    slug = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = ('Campeonato Fase Grupo')
        verbose_name_plural = ('Campeonato Fase Grupos')
        db_table = u'campeonato_fase_grupo'
        
    def __unicode__(self):
        return self.nome
        
class CampeonatoFaseGrupoTabela(models.Model):
    id_campeonato_fase_grupo_tabela = models.AutoField(primary_key=True, serialize=True)
    id_campeonato_fase = models.ForeignKey(CampeonatoFase,
                                           related_name='id_campeonato_fase_grupo_tabela_fase',
                                           db_column='id_campeonato_fase')
    id_campeonato_fase_grupo = models.ForeignKey(CampeonatoFaseGrupo,
                                                 related_name='id_campeonato_fase_grupo_tabela_grupo',
                                                 db_column='id_campeonato_fase_grupo') 
    id_time = models.ForeignKey(Time,
                                related_name='id_campeonato_fase_grupo_tabela_time',
                                db_column='id_time')
    
    pontos = models.SmallIntegerField()
    jogos = models.SmallIntegerField()
    vitorias = models.SmallIntegerField()
    empates = models.SmallIntegerField()
    derrotas = models.SmallIntegerField()
    gols_pro = models.SmallIntegerField()
    cartoes_amarelos = models.SmallIntegerField()
    cartoes_vermelhos = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Campeonato Fase Grupo Tabela')
        verbose_name_plural = ('Campeonato Fase Grupo Tabelas')
        db_table = u'campeonato_fase_grupo_tabela'
        
    def __unicode__(self):
        return str(self.pontos)