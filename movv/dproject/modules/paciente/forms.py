# -*- coding: utf-8 -*-
###############################################################################
# Faz as customizações nas classes de ModelAdmin e as registra no admin do
# django
#
# @author: Alexandre Lavarini Matoso
# @since: 29/10/2012
###############################################################################
from dproject.modules.paciente.models import Nascimento, Paciente
from django import forms
from django.contrib.auth.models import (User, Permission)
from django.contrib.localflavor.br.forms import BRCPFField, BRPhoneNumberField

class NascimentoForm(forms.ModelForm):

    class Meta:
        model = Nascimento

    cpf_pai = BRCPFField(required=True)

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self,*args,**kwargs)

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente

    telefone = BRPhoneNumberField(required=True)

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self,*args,**kwargs)