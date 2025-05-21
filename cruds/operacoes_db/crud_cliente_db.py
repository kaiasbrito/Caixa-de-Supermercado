# LIDA COM O ACESSO AO BANCO DE DADOS
import sqlite3
from utilidades.config import DB_PATH

def buscar_cliente_db(id_cliente):
    """
    Busca um cliente no banco de dados pelo ID.
    Parâmetros:
        id_cliente (int): O ID do cliente a ser buscado.
    Retorna:
        list: Uma lista contendo os dados do cliente encontrado. Se nenhum cliente for encontrado, retorna uma lista vazia.
    """
    # Conecta ao banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM cliente WHERE id_cliente = ?', (id_cliente,))
    cliente = cursor.fetchall()
    
    # Fecha a conexão com o banco de dados e retorna o cliente
    conn.close()
    return cliente

def listar_clientes_db():
    """
    Lista todos os clientes do banco de dados conectando-se ao caminho especificado,
    recuperando os IDs e nomes dos clientes da tabela 'cliente' e exibindo-os no console.
    Retorna:
        None
    """
    # Conecta ao banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Exibe os clientes
    print("\nClientes:")
    cursor.execute("SELECT id_cliente, nome FROM cliente")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]}")
    
    # Fecha a conexão com o banco de dados
    conn.close()
    
def inserir_cliente_db(id_cliente, nome):
    """
    Insere um novo cliente na tabela 'cliente' do banco de dados.
    Parâmetros:
        id_cliente (int): O identificador único do cliente.
        nome (str): O nome do cliente.
    Exceções:
        sqlite3.DatabaseError: Se ocorrer um erro no banco de dados durante a inserção.
    Observação:
        Esta função estabelece uma nova conexão com o banco de dados, insere o cliente,
        realiza o commit da transação e fecha a conexão.
    """
    # Conecta ao banco de dados    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO cliente (id_cliente, nome) VALUES (?, ?)', (id_cliente, nome))
    
    # Salva as alterações e fecha a conexão com o banco de dados
    conn.commit()
    conn.close()
    

