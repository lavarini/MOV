# -*- coding: utf-8 -*-
###############################################################################
# Modulo de gerenciamento
#
# @author: Alexandre Lavarini Matoso
# @since: 29/10/2012
###############################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _


SEXO_CHOICES = (
    ('masculino', 'M'),
    ('feminino', 'F'),
    )

class Paciente(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    prontuario = models.IntegerField()
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateTimeField(null=True, blank=True)
    sexo = models.CharField(_('Sexo'),
        choices=SEXO_CHOICES,
        max_length=1)
    rg = models.IntegerField()
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    cep = models.IntegerField()
    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)

    class Meta:
        verbose_name = ('Paciente')
        verbose_name_plural = ('Pacientes')
        db_table = u'paciente'

    def __unicode__(self):
        return self.nome

class Nascimento(models.Model):
    id_nascimento = models.IntegerField(primary_key=True)
    id_mae = models.ForeignKey(Paciente,
        related_name='id_paciente_mae',
        db_column='id_paciente')
    nome_pai = models.CharField(max_length=255)
    rg_pai = models.IntegerField()
    cpf_pai = models.IntegerField()
    data = models.DateTimeField()
    inicio_gestacao = models.DateTimeField()

    class Meta:
        verbose_name = ('Nascimento')
        verbose_name_plural = ('Nascimentos')
        db_table = u'nascimento'

    def __unicode__(self):
        return self.data