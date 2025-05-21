import sqlite3
from caixa.abrir_caixa import abrir_caixa
import os

def resetar_banco():
    """
    Reseta o banco de dados para o estado original.
    Esta função conecta-se ao banco de dados do supermercado, remove todos os dados das tabelas
    ('item', 'compra', 'cliente', 'produto'), e recarrega os dados iniciais chamando a função 'abrir_caixa'.
    Ao final, exibe uma mensagem indicando que o banco de dados foi restaurado.
    Certifique-se de que a função 'abrir_caixa' está definida e disponível no escopo.
    """
    # Conecta ao banco de dados
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'banco-de-dados', 'mercado-at.db'))
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Remove os dados das tabelas
    cursor.execute("DELETE FROM item")
    cursor.execute("DELETE FROM compra")
    cursor.execute("DELETE FROM cliente")
    cursor.execute("DELETE FROM produto")

    conn.commit()
    conn.close()

    # Carrega os dados novamente
    abrir_caixa()

    print("Banco de dados de volta ao estado original.")
