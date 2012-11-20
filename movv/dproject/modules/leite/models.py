# -*- coding: utf-8 -*-
###############################################################################
# Modulo de gerenciamento
#
# @author: Alexandre Lavarini Matoso
# @since: 29/10/2012
###############################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _
from dproject.modules.paciente.models import Paciente

LEITE_CHOICES = (
    (1, 'Pessimo'),
    (2, 'Ruim'),
    (3, 'Regular'),
    (4, 'Bom'),
    (5, 'Otimo'),
    )

class LeitePrimario(models.Model):
    id_leite = models.AutoField(primary_key=True)
    id_doador = models.ForeignKey(Paciente,
        related_name='id_paciente_doador_leite',
        db_column='id_paciente')
    identificador = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    classificacao = models.IntegerField('Classificacao',
        choices=LEITE_CHOICES,
        max_length=1)
    data = models.DateField()
    pasteurizado = models.BooleanField()

    class Meta:
        verbose_name = ('Leite Primario')
        verbose_name_plural = ('Leites Primarios')
        db_table = u'leite_primario'

    def __unicode__(self):
        return str(self.identificador)
    
class LeiteFinal(models.Model):
    id_leite_final = models.AutoField(primary_key=True)
    id_leite_primario = models.ManyToManyField(LeitePrimario)
    identificador = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    classificacao = models.IntegerField('Classificacao',
        choices=LEITE_CHOICES,
        max_length=1)
    data = models.DateField()

    class Meta:
        verbose_name = ('Leite Final')
        verbose_name_plural = ('Leites Finais')
        db_table = u'leite_final'
        
    def __unicode__(self):
        return str(self.identificador)