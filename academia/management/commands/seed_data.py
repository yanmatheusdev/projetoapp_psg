from datetime import time

from django.core.management.base import BaseCommand

from academia.models import Modalidade, Turma


class Command(BaseCommand):
    help = 'Popula o banco com dados iniciais para a academia.'

    def handle(self, *args, **options):
        if not Modalidade.objects.exists():
            mus = Modalidade.objects.create(
                nome='Musculação',
                descricao='Treino de força e hipertrofia',
                ativa=True,
            )
            nat = Modalidade.objects.create(
                nome='Natação',
                descricao='Aulas em piscina e hidroginástica',
                ativa=True,
            )

            Turma.objects.create(
                modalidade=mus,
                dia_semana=0,
                horario=time(18, 0),
                instrutor='Carla',
                vagas=15,
            )
            Turma.objects.create(
                modalidade=mus,
                dia_semana=2,
                horario=time(19, 0),
                instrutor='João',
                vagas=10,
            )
            Turma.objects.create(
                modalidade=nat,
                dia_semana=4,
                horario=time(17, 30),
                instrutor='Ana',
                vagas=8,
            )

            self.stdout.write(self.style.SUCCESS('Dados iniciais criados com sucesso.'))
        else:
            self.stdout.write(self.style.WARNING('Dados já existem. Nenhuma alteração foi feita.'))
