# Projeto Academia

Sistema de gerenciamento de modalidades e turmas de uma academia.

## Tecnologias

- Python
- Django
- SQLite

## Estrutura do projeto

```text
projetoapp_psg/
├── academia/
│   ├── templates/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   └── admin.py
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
├── venv/
└── README.md
```

## Requisitos

- Python 3.10+
- Django 6.1+

## Como rodar o projeto

Abra o terminal dentro da pasta do projeto:

```powershell
cd "C:\Users\YANMATHEUSMELODOSSAN\Documents\yan matheus\academia-projeto\projetoapp_psg"
```

Crie e ative o ambiente virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install --upgrade pip
a python -m pip install django
```

Aplique as migrações:

```powershell
python manage.py migrate
```

Inicie o servidor:

```powershell
python manage.py runserver
```

Acesse no navegador:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/turmas/

## Como rodar os testes

```powershell
python manage.py test
```

## Funcionalidades

- Cadastro de modalidades
- Cadastro de turmas
- Listagem das modalidades ativas na home
- Listagem da grade de turmas
- Regras de negócio com testes automatizados

## Observações

O projeto usa banco SQLite local e o Django cria um banco temporário para execução de testes, não alterando o banco principal.

