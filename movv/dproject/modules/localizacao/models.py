# -*- coding: utf-8 -*-
###############################################################################
# Modulo de gerenciamento
#
# @author: Alexandre Lavarini Matoso
# @since: 26/04/2010
###############################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _

SOURCE_CHOICES = (
    ('terra', 'terra'),
    ('globo', 'globo'),
    ('uol', 'uol'),
    ('gsm', 'gsm'),
)

class Continente(models.Model):
    id_continente = models.AutoField(primary_key=True, serialize=True)
    nome_pt = models.CharField(max_length=30)
    nome_en = models.CharField(max_length=30)
    nome_es = models.CharField(max_length=30)
    nome_confederacao = models.CharField(max_length=50, null=True, blank=True)
    sigla = models.CharField(max_length=2)
    
    class Meta:
        verbose_name = ('Continente')
        verbose_name_plural = ('Continentes')
        db_table = u'continente'
        
    def __unicode__(self):
        return self.nome_pt

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True, serialize=True)
    id_continente = models.ForeignKey(Continente,
                                      related_name='id_continente_pais',
                                      db_column='id_continente')
    nome_pt = models.CharField(max_length=50)
    nome_en = models.CharField(max_length=50, null=True, blank=True)
    nome_es = models.CharField(max_length=50, null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    populacao = models.FloatField(null=True, blank=True)
    iso3 = models.CharField(max_length=3)
    iso = models.CharField(max_length=2)
    tld = models.CharField(max_length=50, null=True, blank=True)
    codigo_moeda = models.CharField(max_length=500, null=True, blank=True)
    nome_moeda = models.CharField(max_length=500, null=True, blank=True)
    telefone = models.CharField(max_length=500, null=True, blank=True)
    formato_codigo_postal = models.CharField(max_length=500, null=True, blank=True)
    regex_codigo_postal = models.CharField(max_length=500, null=True, blank=True)
    linguagens = models.CharField(max_length=500, null=True, blank=True)
    
    
    class Meta:
        verbose_name = ('Pais')
        verbose_name_plural = ('Paises')
        db_table = u'pais'
        
    def __unicode__(self):
        return self.nome_pt
    
class SourcePais(models.Model):
    id_source_pais = models.AutoField(primary_key=True, serialize=True)
    id_pais = models.ForeignKey(Pais,
                                related_name='id_pais_source',
                                db_column='id_pais')
    tipo = models.CharField(_('Tipo'),
                             choices=SOURCE_CHOICES,
                             max_length=10,
                             help_text='Tipo do source')

    value = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ('Source Pais')
        verbose_name_plural = ('Source Paises')
        db_table = u'source_pais'
        
    def __unicode__(self):
        return self.value

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True, serialize=True)
    id_pais = models.ForeignKey(Pais,
                                related_name='id_pais_estado',
                                db_column='id_pais')
    nome = models.CharField(max_length=150)
    slug = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = ('Estado')
        verbose_name_plural = ('Estados')
        db_table = u'estado'
        
    def __unicode__(self):
        return self.nome

class Cidade(models.Model):
    id_cidade = models.AutoField(primary_key=True, serialize=True)
    id_estado = models.ForeignKey(Estado,
                                  related_name='id_estado_cidade',
                                  db_column='id_estado')
    nome = models.CharField(max_length=150)
    capital = models.SmallIntegerField()
    
    class Meta:
        verbose_name = ('Cidade')
        verbose_name_plural = ('Cidades')
        db_table = u'cidade'
        
    def __unicode__(self):
        return self.nome