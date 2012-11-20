# -*- coding: utf-8 -*-
###############################################################################
# Modulo de gerenciamento
#
# @author: Alexandre Lavarini Matoso
# @since: 29/10/2012
###############################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    prontuario = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=255, unique=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = ('Paciente')
        verbose_name_plural = ('Pacientes')
        db_table = u'paciente'

    def __unicode__(self):
        return self.nome

class Nascimento(models.Model):
    id_nascimento = models.AutoField(primary_key=True)
    id_mae = models.ForeignKey(Paciente,
        related_name='id_paciente_mae',
        db_column='id_paciente')
    nome_pai = models.CharField(max_length=255, null=True, blank=True)
    rg_pai = models.CharField(max_length=255, null=True, blank=True)
    cpf_pai = models.CharField(max_length=255, null=True, blank=True)
    data = models.DateField()
    inicio_gestacao = models.DateField()

    class Meta:
        verbose_name = ('Bebe')
        verbose_name_plural = ('Bebes')
        db_table = u'nascimento'

    def __unicode__(self):
        return str(self.data)