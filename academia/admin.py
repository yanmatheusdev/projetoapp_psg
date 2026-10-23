from django.contrib import admin

from .models import Modalidade, Turma


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "ativa")   
    list_filter = ("ativa",)           
    search_fields = ("nome",)


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ("modalidade", "dia_semana", "horario_24h", "instrutor", "vagas")  
    list_filter = ("modalidade", "dia_semana")                                         
    search_fields = ("instrutor",)                                                     

    @admin.display(description="horário", ordering="horario")
    def horario_24h(self, obj):
        return obj.horario.strftime("%H:%M")