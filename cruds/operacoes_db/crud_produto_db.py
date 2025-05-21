import sqlite3
from utilidades.config import DB_PATH

def buscar_produto_db(id_produto):
    """
    Busca um produto no banco de dados pelo seu ID.
    Parâmetros:
        id_produto (int): O ID do produto a ser buscado.
    Retorna:
        tuple or None: Uma tupla contendo (id_produto, nome, quantidade, preco) se o produto for encontrado,
        ou None caso não exista um produto com o ID informado.
    """
    # Conecta ao banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_produto, nome, quantidade, preco FROM produto WHERE id_produto = ?", (id_produto,))
    produto = cursor.fetchone()
    
    # Fecha a conexão com o banco de dados
    conn.close()
    return produto


def listar_produtos_db():
    """
    Recupera uma lista de produtos do banco de dados.
    Conecta ao banco de dados, busca todos os produtos com seus IDs, nomes, quantidades e preços,
    e os retorna como uma lista de tuplas.
    Retorna:
        list of tuple: Cada tupla contém (id_produto, nome, quantidade, preco) de um produto.
    """
    # Conecta ao banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Exibe os clientes
    print("\nProdutos:")
    cursor.execute("SELECT id_produto, nome, quantidade, preco FROM produto")
    produtos = cursor.fetchall()
    return produtos
        
    # Fecha a conexão com o banco de dados
    conn.close()
    

def atualizar_estoque_db(id_produto, nova_quantidade):
    """
    Atualiza a quantidade em estoque de um produto no banco de dados.

    Parâmetros:
        id_produto (int): O identificador único do produto a ser atualizado.
        nova_quantidade (int): A nova quantidade em estoque para o produto.

    Retorna:
        None
    """
    # Conecta ao banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('UPDATE produto SET quantidade = ? WHERE id_produto = ?', (nova_quantidade, id_produto))

    # Salva as mudanças e fecha a conexão com o banco de dados
    conn.commit()
    conn.close()
