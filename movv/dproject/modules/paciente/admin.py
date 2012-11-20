# -*- encoding: utf-8 -*-
################################################################################
# Administração do módulo pacientes
#
# @author: Alexandre Lavarini Matoso
# @since: 31/03/2011
################################################################################
import datetime
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from dproject.modules.paciente.models import Paciente, Nascimento
from django.contrib.admin import SimpleListFilter

class NascimentoFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Gestacao'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'nascimento'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('antes', 'Antes de 32 semanas'),
            ('depois', 'Depois de 32 semanas'),
            )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        semanas = (datetime.date.today() - datetime.timedelta(7*32))
        if self.value() == 'antes':
            return queryset.filter(inicio_gestacao__gt=semanas)
        if self.value() == 'depois':
            return queryset.filter(inicio_gestacao__lt=semanas)

class PacienteAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Paciente'

    #form = FontesCampeonatosForm
    search_fields = ('nome', 'prontuario', 'cpf')
    ordering = ['-id_paciente']
    list_display = ('prontuario', 'nome', 'data_nascimento', 'rg', 'cpf', 'telefone', 'cidade')

class NascimentoAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        verbose_name = 'Bebe'

    search_fields = ('nome_pai', 'inicio_gestacao', 'data', 'id_mae__nome', 'id_mae__cpf', 'id_mae__rg',)
    ordering = ['-id_nascimento']
    list_display = ('inicio_gestacao', 'id_mae', 'data',)
    raw_id_fields = ('id_mae', )
    list_filter = (NascimentoFilter,)

#class DoadorAdmin(admin.ModelAdmin):
#    """
#    """
#    class Meta:
#        verbose_name = 'Doador'
#
#    search_fields = ('id_paciente__nome', 'id_paciente__prontuario', 'id_paciente__cpf')
#    ordering = ['-id_doador']
#    list_display = ('id_paciente__nome', 'id_paciente__cpf', )
    #raw_id_fields = ('id_paciente', )


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Nascimento, NascimentoAdmin)
#admin.site.register(Doador, DoadorAdmin)

