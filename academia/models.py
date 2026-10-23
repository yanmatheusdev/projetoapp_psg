from django.db import models


class Modalidade(models.Model):
    nome = models.CharField(max_length=60, unique=True)  # RN07
    descricao = models.TextField("descrição", blank=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "modalidade"
        verbose_name_plural = "modalidades"

    def __str__(self):
        return self.nome


class Turma(models.Model):
    DIAS = [
        (0, "Segunda"),
        (1, "Terça"),
        (2, "Quarta"),
        (3, "Quinta"),
        (4, "Sexta"),
        (5, "Sábado"),
    ]
    
    modalidade = models.ForeignKey(
        Modalidade, on_delete=models.PROTECT, related_name="turmas"
    )
    dia_semana = models.PositiveSmallIntegerField("dia da semana", choices=DIAS)
    horario = models.TimeField("horário")  # RN05
    instrutor = models.CharField(max_length=100)
    vagas = models.PositiveIntegerField(default=10)  # RN06

    class Meta:
        ordering = ["dia_semana", "horario"]
        verbose_name = "turma"
        verbose_name_plural = "turmas"

    def __str__(self):
        return f"{self.modalidade.nome} — {self.get_dia_semana_display()} {self.horario:%H:%M}"