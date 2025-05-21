import sqlite3
from utilidades.config import DB_PATH

def inserir_item(quantidade, id_compra, id_produto):
    """
    Insere um novo item na tabela 'item' do banco de dados.
    Parâmetros:
        quantidade (int): A quantidade do produto a ser inserida.
        id_compra (int): O identificador da compra associada ao item.
        id_produto (int): O identificador do produto a ser inserido.
    Exceções:
        Imprime uma mensagem de erro caso ocorra qualquer exceção durante a operação de inserção no banco de dados.
    """
    try:
        # Conecta ao banco de dados
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Insere o item 
        cursor.execute(
        'INSERT INTO item (quantidade, id_compra, id_produto) VALUES (?, ?, ?)',
        (quantidade, id_compra, id_produto)
    )
        # Salva as alterações
        conn.commit()

        # Fecha a conexão
        conn.close()
    
    except Exception as e:
        print(f"Erro ao adicionar item ao banco de dados: {e}")


def atualizar_estoque(id_produto, quantidade):
    """
    Atualiza o estoque de um produto subtraindo uma quantidade específica.
    Parâmetros:
        id_produto (int): O identificador único do produto cujo estoque será atualizado.
        quantidade (int): A quantidade a ser subtraída do estoque atual do produto.
    Esta função conecta-se ao banco de dados, atualiza o campo 'quantidade' do produto especificado e salva as alterações.
    """
    # Conecta ao banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(
        'UPDATE produto SET quantidade = quantidade - ? WHERE id_produto = ?',
        (quantidade, id_produto)
    )
    # Salva as alterações e fecha a conexão com o banco de dados
    conn.commit()
    conn.close()
    
    
def listar_itens_por_compra_db(id_compra):
    """
    Recupera uma lista de itens associados a uma compra específica no banco de dados.
    Parâmetros:
        id_compra (int): O ID da compra para a qual os itens serão recuperados.
    Retorna:
        list of tuple: Uma lista de tuplas, cada uma contendo o nome do produto (str), quantidade (int) e preço (float)
        para cada item da compra especificada.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT p.nome, i.quantidade, p.preco
        FROM item i
        JOIN produto p ON i.id_produto = p.id_produto
        WHERE i.id_compra = ?
    """, (id_compra,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado
