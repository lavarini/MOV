# -*- coding: utf-8 -*-
###############################################################################
# Modulo de gerenciamento
#
# @author: Alexandre Lavarini Matoso
# @since: 04/05/2011
###############################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _
from futebol.modules.localizacao.models import Cidade, Estado, Pais

TIME_CHOICES = (
    ('clube', 'clube'),
    ('selecao', 'selecao'),
)

SOURCE_CHOICES = (
    ('terra', 'terra'),
    ('globo', 'globo'),
    ('uol', 'uol'),
    ('gsm', 'gsm'),
)

MUSICA_CHOICES = (
    ('hino', 'hino'),
    ('grito_torcida', 'grito_torcida'),
)

class Time(models.Model):
    id_time = models.AutoField(primary_key=True, serialize=True)
    id_pais = models.ForeignKey(Pais,
                                related_name='id_pais_time',
                                db_column='id_pais')
    id_estado = models.ForeignKey(Estado,
                                  related_name='id_estado_time',
                                  db_column='id_estado')
    id_cidade = models.ForeignKey(Cidade,
                                  related_name='id_cidade_time',
                                  db_column='id_cidade')
    
    tipo = models.CharField(_('Tipo'),
                             choices=TIME_CHOICES,
                             max_length=10,
                             help_text='Tipo do time, seleção ou clube')
    
    nome_completo = models.CharField(max_length=50)
    nome_popular = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    nome_lista = models.CharField(max_length=45, null=True, blank=True)
    slug = models.CharField(max_length=45)
    nome_torcedor_singular = models.CharField(max_length=100, null=True, blank=True)
    nome_torcedor_plural = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = ('Time')
        verbose_name_plural = ('Times')
        db_table = u'time'
        
    def __unicode__(self):
        return self.nome_popular
    
class SourceTime(models.Model):
    id_source_time = models.AutoField(primary_key=True, serialize=True)
    id_time = models.ForeignKey(Time,
                                related_name='id_time_source',
                                db_column='id_time')

    value = models.CharField(max_length=100)
    tipo = models.CharField(_('Tipo'),
                             choices=SOURCE_CHOICES,
                             max_length=10,
                             help_text='Tipo do source')
    
    class Meta:
        verbose_name = ('Source Time')
        verbose_name_plural = ('Source Times')
        db_table = u'source_time'
    
    def __unicode__(self):
        return self.value
    
class TimeMusica(models.Model):
    id_time_musica = models.AutoField(primary_key=True, serialize=True)
    id_time = models.ForeignKey(Time,
                                related_name='id_musica_time',
                                db_column='id_time')

    url = models.CharField(max_length=45, null=True, blank=True)    
    tipo = models.CharField(_('Tipo'),
                             choices=MUSICA_CHOICES,
                             max_length=20)
    id_letra_letrasmusbr = models.SmallIntegerField()
    id_video_aula = models.CharField(max_length=45, null=True, blank=True)
    ativo = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Time Musica')
        verbose_name_plural = ('Times Musicas')
        db_table = u'time_musica'
        
    def __unicode__(self):
        return str(self.id_time_musica)