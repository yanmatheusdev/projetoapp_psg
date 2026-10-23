from django.shortcuts import render

from .models import Modalidade, Turma

ACADEMIA = {
    "nome": "Academia Corpo em Movimento",
    "endereco": "Rua Exemplo, 123 - Centro, Caruaru - PE",
    "telefone": "(81) 99999-0000",
}


def home(request):  
    modalidades = Modalidade.objects.filter(ativa=True)
    return render(
        request, "academia/home.html", {"academia": ACADEMIA, "modalidades": modalidades}
    )


def grade(request):  
    turmas = Turma.objects.select_related("modalidade")
    return render(
        request, "academia/grade.html", {"academia": ACADEMIA, "turmas": turmas}
    )