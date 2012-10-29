# -*- coding: utf-8 -*-
###############################################################################
# Modulo de gerenciamento
#
# @author: Alexandre Lavarini Matoso
# @since: 17/06/2011
###############################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _
from futebol.modules.time.models import Time
from futebol.modules.campeonato.models import Campeonato

IDIOMA_CHOICES = (
    ('pt', 'pt'),
    ('en', 'en'),
    ('es', 'es'),
)

class SourceNoticia(models.Model):
    id_source_noticia = models.AutoField(primary_key=True, serialize=True)
    tipo = models.CharField(max_length=100)
    idioma = models.CharField(_('Idioma'),
                             choices=IDIOMA_CHOICES,
                             max_length=10)
    
    class Meta:
        verbose_name = ('Source Noticia')
        verbose_name_plural = ('Source Noticias')
        db_table = u'source_noticia'
        
    def __unicode__(self):
        return self.tipo

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True, serialize=True)
    id_source_noticia = models.ForeignKey(SourceNoticia,
                                          related_name='id_source_noticia_noticia',
                                          db_column='id_source_noticia')
    idioma = models.CharField(_('Idioma'),
                             choices=IDIOMA_CHOICES,
                             max_length=10)
    url = models.CharField(max_length=300)
    data = models.DateTimeField()
    lead = models.TextField()
    manchete = models.CharField(max_length=300)
    thumbnail_grande = models.CharField(max_length=100,
                                        null=True, blank=True)
    thumbnail_pequeno = models.CharField(max_length=100,
                                         null=True, blank=True)
    corpo = models.TextField(null=True, blank=True)
    id_noticia_eusou = models.SmallIntegerField(null=True, blank=True)
    flag_corpo = models.SmallIntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = ('Noticia')
        verbose_name_plural = ('Noticias')
        db_table = u'noticia'
        
    def __unicode__(self):
        return str(self.manchete)

class NoticiaTime(models.Model):
    id_noticia_time = models.AutoField(primary_key=True, serialize=True)
    id_noticia = models.ForeignKey(Noticia,
                                   related_name='id_noticia_noticia_time',
                                   db_column='id_noticia')
    id_time = models.ForeignKey(Time,
                                related_name='id_time_noticia',
                                db_column='id_time')
    data_insercao = models.DateTimeField()
    visitas = models.SmallIntegerField()
    last_ip = models.CharField(max_length=15,
                               null=True, blank=True)
    
    class Meta:
        verbose_name = ('Noticia Time')
        verbose_name_plural = ('Noticias Times')
        db_table = u'noticia_time'
        
    def __unicode__(self):
        return str(self.id_noticia_time)

class NoticiaTimeView(models.Model):
    id_noticia_time = models.AutoField(primary_key=True, serialize=True)
    id_noticia = models.SmallIntegerField()
    id_time = models.SmallIntegerField()
    data_insercao = models.DateTimeField()
    visitas = models.SmallIntegerField()
    last_ip = models.CharField(max_length=15,
                               null=True, blank=True)
    
    class Meta:
        verbose_name = ('Noticia Time View')
        verbose_name_plural = ('Noticias Times View')
        db_table = u'noticia_time'
        
    def __unicode__(self):
        return str(self.id_noticia_time)

class NoticiaCampeonato(models.Model):
    id_noticia_campeonato = models.AutoField(primary_key=True, serialize=True)
    id_noticia = models.SmallIntegerField()
    id_campeonato = models.SmallIntegerField()
    data_insercao = models.DateTimeField()
    visitas = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Noticia Campeonato')
        verbose_name_plural = ('Noticias Campeonatos')
        db_table = u'noticia_campeonato'
        
    def __unicode__(self):
        return str(self.id_noticia_campeonato)

class NoticiaCampeonatoView(models.Model):
    id_noticia_campeonato = models.AutoField(primary_key=True, serialize=True)
    id_noticia = models.ForeignKey(Noticia,
                                   related_name='id_noticia_campeonato_noticia',
                                   db_column='id_noticia')
    id_campeonato = models.ForeignKey(Time,
                                      related_name='id_campeonato_noticia',
                                      db_column='id_campeonato')
    data_insercao = models.DateTimeField()
    visitas = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Noticia Campeonato View')
        verbose_name_plural = ('Noticias Campeonatos View')
        db_table = u'noticia_campeonato'
        
    def __unicode__(self):
        return str(self.id_noticia_campeonato)
    
