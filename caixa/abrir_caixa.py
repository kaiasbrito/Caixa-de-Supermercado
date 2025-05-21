import sqlite3
import csv
import os
from datetime import datetime
from utilidades.config import DB_PATH

def abrir_caixa():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CLIENTES_CSV = os.path.abspath(os.path.join(BASE_DIR, '..', 'banco-de-dados', 'clientes.csv'))
    PRODUTOS_CSV = os.path.abspath(os.path.join(BASE_DIR, '..', 'banco-de-dados', 'produtos.csv'))

    def criar_db():
        """
        Cria as tabelas necessárias no banco de dados SQLite para o sistema de caixa do supermercado, caso ainda não existam.
        Tabelas criadas:
        - cliente: Armazena informações dos clientes.
        - produto: Armazena detalhes dos produtos, incluindo nome, quantidade e preço.
        - compra: Armazena registros de compras, referenciando o cliente.
        - item: Armazena itens de uma compra, referenciando tanto a compra quanto o produto.
        Não recebe argumentos.
        Não retorna valor.
        """
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS produto (
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS compra (
            id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
            data_compra TEXT NOT NULL, 
            id_cliente INTEGER NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
        )''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS item (
            id_item INTEGER PRIMARY KEY AUTOINCREMENT,
            quantidade INTEGER NOT NULL,
            id_compra INTEGER NOT NULL,
            id_produto INTEGER NOT NULL,
            FOREIGN KEY (id_compra) REFERENCES compra(id_compra),
            FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
        )''')

        conn.commit()
        conn.close()

    def carregar_csv():
        """
        Carrega dados de clientes e produtos a partir de arquivos CSV para o banco de dados SQLite, caso ainda não existam.
        Esta função lê informações de clientes e produtos dos arquivos CSV especificados por CLIENTES_CSV e PRODUTOS_CSV.
        Para cada entrada nos arquivos CSV, verifica se o registro já existe na tabela correspondente do banco de dados
        ('cliente' ou 'produto'). Se o registro não existir, insere o novo registro no banco de dados.
        Retorna:
            None
        """
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        with open(CLIENTES_CSV, 'r', encoding='utf-8') as arquivo_clientes:
            leitor_clientes = csv.reader(arquivo_clientes)
            for linha in leitor_clientes:
                id_cliente, nome = linha
                cursor.execute("SELECT id_cliente FROM cliente WHERE id_cliente = ?", (id_cliente,))
                if not cursor.fetchone():
                    cursor.execute("INSERT INTO cliente (id_cliente, nome) VALUES (?, ?)", (id_cliente, nome))

        with open(PRODUTOS_CSV, 'r', encoding='utf-8') as arquivo_produtos:
            leitor_produtos = csv.reader(arquivo_produtos)
            for linha in leitor_produtos:
                id_produto, nome, quantidade, preco = linha
                cursor.execute("SELECT id_produto FROM produto WHERE id_produto = ?", (id_produto,))
                if not cursor.fetchone():
                    cursor.execute("INSERT INTO produto (id_produto, nome, quantidade, preco) VALUES (?, ?, ?, ?)",
                                   (id_produto, nome, quantidade, preco))

        conn.commit()
        conn.close()

    def exibir_dados():
        """
        Exibe dados das tabelas 'cliente' e 'produto' no banco de dados do supermercado.
        Esta função conecta ao banco de dados SQLite, recupera e imprime uma lista de clientes (com seus IDs e nomes)
        e uma lista de produtos (com seus IDs, nomes, quantidades e preços). Também imprime a data e hora atual
        indicando quando o caixa foi aberto.
        Retorna:
            bool: Sempre retorna True após exibir os dados.
        """
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        print("Clientes:")
        cursor.execute("SELECT id_cliente, nome FROM cliente")
        for cliente in cursor.fetchall():
            print(f"ID: {cliente[0]} | Nome: {cliente[1]}")

        print("\nProdutos:")
        cursor.execute("SELECT id_produto, nome, quantidade, preco FROM produto")
        for produto in cursor.fetchall():
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Preço: R$ {produto[3]}")

        conn.close()

        data_abertura = datetime.now().strftime("%d/%m/%Y %H:%M")
        print("\nCaixa aberto em: ", data_abertura)
        return True

    criar_db()
    carregar_csv()
    return exibir_dados()
