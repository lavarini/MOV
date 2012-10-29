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
from futebol.modules.pessoa.models import Pessoa
from futebol.modules.jogo.models import EventoJogo

IDIOMA_CHOICES = (
    ('pt', 'pt'),
    ('en', 'en'),
    ('es', 'es'),
)

TIPO_CHOICES = (
    ('youtube', 'youtube'),
    ('sportv_id', 'sportv_id'),
    ('sportv_url', 'sportv_url'),
)

class SourceVideo(models.Model):
    id_source_video = models.AutoField(primary_key=True, serialize=True)
    tipo = models.CharField(_('Tipo'),
                             choices=TIPO_CHOICES,
                             max_length=20)
    idioma = models.CharField(_('Idioma'),
                             choices=IDIOMA_CHOICES,
                             max_length=10)
    
    class Meta:
        verbose_name = ('Source Video')
        verbose_name_plural = ('Source Videos')
        db_table = u'source_video'
        
    def __unicode__(self):
        return self.tipo
    
class VideoCategoria(models.Model):
    id_video_categoria = models.AutoField(primary_key=True, serialize=True)
    nome = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)
    
    class Meta:
        verbose_name = ('Video Categoria')
        verbose_name_plural = ('Videos Categorias')
        db_table = u'video_categoria'
        
    def __unicode__(self):
        return self.nome    

class Video(models.Model):
    id_video = models.AutoField(primary_key=True, serialize=True)
    id_source_video = models.ForeignKey(SourceVideo,
                                        related_name='id_source_video_video',
                                        db_column='id_source_video')
    id_video_categoria = models.ForeignKey(VideoCategoria,
                                           related_name='id_video_categoria_video',
                                           db_column='id_video_categoria')
    idioma = models.CharField(_('Idioma'),
                             choices=IDIOMA_CHOICES,
                             max_length=10)
    url = models.CharField(max_length=200)
    data = models.DateTimeField(null=True, blank=True)
    titulo = models.CharField(max_length=300)
    descricao = models.CharField(max_length=500)
    duracao = models.SmallIntegerField()
    thumbnail_grande = models.CharField(max_length=100,
                                        null=True, blank=True)
    thumbnail_pequeno = models.CharField(max_length=100,
                                         null=True, blank=True)
    id_video_eusou = models.SmallIntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = ('Video')
        verbose_name_plural = ('Videos')
        db_table = u'video'
        
    def __unicode__(self):
        return self.titulo

class VideoTime(models.Model):
    id_video_time = models.AutoField(primary_key=True, serialize=True)
    id_video = models.ForeignKey(Video,
                                 related_name='id_video_video_time',
                                 db_column='id_video')
    id_time = models.ForeignKey(Time,
                                related_name='id_time_video',
                                db_column='id_time')
    data_insercao = models.DateTimeField()
    visualizacoes = models.SmallIntegerField()
    last_ip = models.CharField(max_length=15,
                               null=True, blank=True)
    
    class Meta:
        verbose_name = ('Video Time')
        verbose_name_plural = ('Videos Times')
        db_table = u'video_time'
        
    def __unicode__(self):
        return str(self.id_noticia_time)

class VideoPessoa(models.Model):
    id_video_pessoa = models.AutoField(primary_key=True, serialize=True)
    id_video = models.ForeignKey(Video,
                                 related_name='id_video_video_pessoa',
                                 db_column='id_video')
    id_pessoa = models.ForeignKey(Pessoa,
                                  related_name='id_pessoa_video',
                                  db_column='id_pessoa')
    data_insercao = models.DateTimeField()
    visualizacoes = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Video Pessoa')
        verbose_name_plural = ('Videos Pessoas')
        db_table = u'video_pessoa'
        
    def __unicode__(self):
        return str(self.id_video_pessoa)

class VideoEventoJogo(models.Model):
    id_video_evento_jogo = models.AutoField(primary_key=True, serialize=True)
    id_video = models.ForeignKey(Video,
                                 related_name='id_video_video_evento_jogo',
                                 db_column='id_video')
    id_evento_jogo = models.ForeignKey(EventoJogo,
                                       related_name='id_evento_jogo_video',
                                       db_column='id_evento_jogo')
    data_insercao = models.DateTimeField()
    visualizacoes = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Video Evento Jogo')
        verbose_name_plural = ('Videos Eventos Jogo')
        db_table = u'video_evento_jogo'
        
    def __unicode__(self):
        return str(self.id_video_evento_jogo)
