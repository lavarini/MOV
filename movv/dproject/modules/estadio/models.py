# -*- coding: utf-8 -*-
###############################################################################
# Modulo de gerenciamento
#
# @author: Alexandre Lavarini Matoso
# @since: 02/05/2011
###############################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _
from futebol.modules.localizacao.models import Cidade
from futebol.modules.time.models import Time

SOURCE_CHOICES = (
    ('terra', 'terra'),
    ('globo', 'globo'),
    ('uol', 'uol'),
    ('gsm', 'gsm'),
)

class Estadio(models.Model):
    id_estadio = models.AutoField(primary_key=True, serialize=True)
    id_cidade = models.ForeignKey(Cidade,
                                  related_name='id_cidade_estadio',
                                  db_column='id_cidade')
    data_inauguracao = models.DateField(null=True, blank=True)
    medida_h = models.SmallIntegerField(null=True, blank=True)
    medida_w = models.SmallIntegerField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    nome_popular = models.CharField(max_length=50, null=True, blank=True)
    lotacao = models.IntegerField(null=True, blank=True)
    arquiteto = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    endereco_cep = models.IntegerField(null=True, blank=True)
    endereco_complemento = models.CharField(max_length=20, null=True, blank=True)
    endereco_numero = models.IntegerField(null=True, blank=True)
    
    
    class Meta:
        verbose_name = ('Estadio')
        verbose_name_plural = ('Estadios')
        db_table = u'estadio'
        
    def __unicode__(self):
        return self.nome
    
class SourceEstadio(models.Model):
    id_source_estadio = models.AutoField(primary_key=True, serialize=True)
    id_estadio = models.ForeignKey(Estadio,
                                   related_name='id_estadio_source',
                                   db_column='id_estadio')
    tipo = models.CharField(_('Tipo'),
                             choices=SOURCE_CHOICES,
                             max_length=10,
                             help_text='Tipo do source')

    value = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = ('Source Estadio')
        verbose_name_plural = ('Source Estadios')
        db_table = u'source_estadio'
        
    def __unicode__(self):
        return self.value
    
class EstadioTime(models.Model):
    id_estadio_time = models.AutoField(primary_key=True, serialize=True)
    id_time = models.ForeignKey(Time,
                                related_name='id_time_estadio',
                                db_column='id_time')
    id_estadio = models.ForeignKey(Estadio,
                                   related_name='id_estadio_time',
                                   db_column='id_estadio')
    
    class Meta:
        verbose_name = ('Estadio Time')
        verbose_name_plural = ('Estadios Times')
        db_table = u'estadio_time'
        
    def __unicode__(self):
        return str(self.id_estadio_time)