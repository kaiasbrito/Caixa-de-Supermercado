import sqlite3
from utilidades.config import DB_PATH
 
def criar_compra_db(id_cliente, data_compra):
    """
    Cria um novo registro de compra no banco de dados.
    Args:
        id_cliente (int): O ID do cliente que está realizando a compra.
        data_compra (str): A data da compra no formato 'YYYY-MM-DD' ou equivalente.
    Returns:
        int: O ID da compra recém-criada (gerado automaticamente pelo banco de dados).
    """
    # Conecta ao banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO compra (data_compra, id_cliente) VALUES (?, ?)', (data_compra, id_cliente))
    conn.commit()
    id_compra = cursor.lastrowid # obtém o ID da compra mais recente criada pelo autoincremento 
    
    # Fecha a conexão com o banco de dados e retorna o ID da compra
    conn.close()
    return id_compra

def inserir_item_db(quantidade, id_compra, id_produto):
    """
    Insere um novo item na tabela 'item' do banco de dados.
    Parâmetros:
        quantidade (int): A quantidade do produto a ser inserida.
        id_compra (int): O ID da compra à qual o item está associado.
        id_produto (int): O ID do produto a ser inserido.
    Retorna:
        None
    """
    # Conecta ao banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Insere o item 
    cursor.execute(
        'INSERT INTO item (quantidade, id_compra, id_produto) VALUES (?, ?, ?)',
        (quantidade, id_compra, id_produto)
    )
    
    # Salva as alterações e fecha a conexão com o banco de dados
    conn.commit()
    conn.close()

def total_vendas_db():
    """
    Calcula o valor total das vendas registradas no banco de dados.

    Esta função conecta-se ao banco de dados SQLite definido por DB_PATH, realiza um JOIN entre as tabelas 'item' e 'produto',

        float: O valor total das vendas. Retorna 0.0 caso não existam vendas registradas.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(i.quantidade * p.preco)
        FROM item i
        JOIN produto p ON i.id_produto = p.id_produto
    """)
    total = cursor.fetchone()[0] or 0.0
    conn.close()
    return total

def vendas_por_cliente_db():
    """
    Recupera o número total de itens e o valor total de vendas para cada cliente.

    Realiza um join SQL entre as tabelas 'compra', 'cliente', 'item' e 'produto' para calcular, para cada cliente:
    - A quantidade total de itens comprados.
    - O valor total das compras.

    Retorna:
        lista de tuplas: Cada tupla contém (id_cliente, nome, total_itens, total_valor), ordenadas por total_valor em ordem decrescente.
    """
    # Realiza o join entre as tabelas compra, cliente, item e produto e calcula o total de vendas por cliente
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            c.id_cliente,
            cl.nome,
            SUM(i.quantidade)        AS total_itens,
            SUM(i.quantidade * p.preco) AS total_valor
        FROM compra c
        JOIN cliente cl ON c.id_cliente = cl.id_cliente
        JOIN item i    ON i.id_compra = c.id_compra
        JOIN produto p ON i.id_produto = p.id_produto
        GROUP BY c.id_cliente, cl.nome
        ORDER BY total_valor DESC
    """)
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def produtos_fora_de_estoque_db():
    """
    Recupera uma lista de produtos que estão fora de estoque no banco de dados.

    Retorna:
        lista de tuplas: Cada tupla contém o nome e a quantidade de um produto
        cuja quantidade é menor ou igual a zero.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.nome, p.quantidade
        FROM produto p
        WHERE p.quantidade <= 0
    """)

    resultado = cursor.fetchall()
    conn.close()
    return resultado

def buscar_compra_db(id_compra):
    """
    Busca o ID do cliente e a data da compra para um determinado ID de compra no banco de dados.

    Args:
        id_compra (int): O identificador único da compra a ser recuperada.

    Retorna:
        tuple ou None: Uma tupla contendo (id_cliente, data_compra) se a compra for encontrada,
                       ou None se nenhum registro correspondente existir.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id_cliente, data_compra FROM compra WHERE id_compra = ?", (id_compra,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

