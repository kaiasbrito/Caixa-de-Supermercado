import os
"""
Este módulo fornece utilitários de configuração para o projeto 'supermercado'.
Atributos:
    BASE_DIR (str): O caminho absoluto para o diretório base do projeto ('supermercado').
    DB_PATH (str): O caminho absoluto para o arquivo do banco de dados SQLite ('mercado-at.db') localizado no diretório 'banco-de-dados'.
"""

# Caminho base do projeto (pasta "supermercado")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho absoluto do banco de dados
DB_PATH = os.path.join(BASE_DIR, 'banco-de-dados', 'mercado-at.db')
