from datetime import time

from django.db.models import ProtectedError
from django.test import TestCase
from django.urls import reverse

from .models import Modalidade, Turma


class RegrasTest(TestCase):
    def setUp(self):
        self.musc = Modalidade.objects.create(nome="Musculação", descricao="Pesos")
        self.nat = Modalidade.objects.create(nome="Natação", ativa=False)
        Turma.objects.create(modalidade=self.musc, dia_semana=1, horario=time(18, 0), instrutor="Carla", vagas=15)
        Turma.objects.create(modalidade=self.musc, dia_semana=0, horario=time(19, 0), instrutor="Carla", vagas=15)

    def test_nao_exclui_modalidade_com_turmas(self):  # RN03
        with self.assertRaises(ProtectedError):
            self.musc.delete()

    def test_str_da_turma(self):
        t = Turma.objects.get(dia_semana=0)
        self.assertEqual(str(t), "Musculação — Segunda 19:00")

    def test_home_nao_mostra_inativa(self):  # RN08
        resp = self.client.get(reverse("home"))
        self.assertContains(resp, "Musculação")
        self.assertNotContains(resp, "Natação")

    def test_grade_ordenada(self):  # RF07
        resp = self.client.get(reverse("grade"))
        dias = [t.dia_semana for t in resp.context["turmas"]]
        self.assertEqual(dias, sorted(dias))