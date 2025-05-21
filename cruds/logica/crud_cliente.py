from cruds.operacoes_db.crud_cliente_db import (buscar_cliente_db, listar_clientes_db, inserir_cliente_db)

# Interação com o usuário e tratamento de erros

def buscar_cliente(id_cliente):
    """
    Busca um cliente pelo seu ID.

    Parâmetros:
        id_cliente (str): O ID do cliente a ser buscado. Deve ser uma string numérica.

    Retorna:
        dict ou None: Retorna um dicionário com os dados do cliente se encontrado, 
        ou None se o ID for inválido ou o cliente não for encontrado.

    Exibe:
        Mensagem de erro se o ID fornecido não for numérico.
    """
    if not id_cliente.isdigit():
        print("Erro: id inválido")
        return None
    cliente = buscar_cliente_db(id_cliente)
    return cliente

def exibir_clientes():
    """
    Exibe a lista de clientes cadastrados.

    Recupera os clientes do banco de dados utilizando a função listar_clientes_db().
    Se não houver clientes cadastrados, informa o usuário.
    Caso contrário, imprime o ID e o nome de cada cliente cadastrado.
    """
    clientes = listar_clientes_db()
    if not clientes:
        print("Não há clientes cadastrados.")
    else:
        print("\nClientes cadastrados:")
        for i in clientes:
            print(f"ID: {i[0]} | Nome: {i[1]}")
            
def cadastrar_cliente():
    """
    Cadastra um novo cliente no sistema.
    Solicita ao usuário o ID e o nome do cliente, valida os dados informados e verifica se o cliente já está cadastrado.
    Se o ID for um número e o nome não estiver vazio, e o cliente ainda não existir, insere o cliente no banco de dados.
    Exibe mensagens apropriadas em caso de erro ou sucesso.
    Exceções:
        Exibe uma mensagem de erro caso ocorra qualquer exceção durante o cadastro.
    Dependências:
        - buscar_cliente(id_cliente): Função que verifica se o cliente já está cadastrado.
        - inserir_cliente_db(id_cliente, nome): Função que insere o cliente no banco de dados.
    """
    try:
        id_cliente = input("Digite o ID do cliente: ")
        nome = input("Digite o nome do cliente: ")

        if not id_cliente.isdigit():
            print("Erro: ID do cliente deve ser um número.")
            return

        if not nome.strip():
            print("Erro: Nome do cliente não pode estar vazio.")
            return

        if buscar_cliente(id_cliente):
            print("Cliente já está cadastrado.")
        else:
            inserir_cliente_db(int(id_cliente), nome)
            print("Cliente cadastrado com sucesso.")
            
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar o cliente: {e}")