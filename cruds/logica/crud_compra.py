from cruds.operacoes_db.crud_compra_db import vendas_por_cliente_db, produtos_fora_de_estoque_db, criar_compra_db
from cruds.operacoes_db.crud_compra_db import criar_compra_db

from datetime import datetime

def vendas_por_cliente():
    """
    Recupera e retorna a lista de vendas por cliente.

    Busca os dados de vendas no banco de dados usando a função vendas_por_cliente_db.
    Se nenhuma venda for encontrada, exibe uma mensagem e retorna uma lista vazia.

    Retorna:
        list: Uma lista de vendas por cliente, ou uma lista vazia se não houver vendas registradas.
    """
    vendas = vendas_por_cliente_db()
    if not vendas:
        print("Nenhuma venda registrada.")
        return []
    return vendas
        
def produtos_fora_de_estoque():
    """
    Recupera e exibe produtos que estão fora de estoque.

    Esta função chama a função `produtos_fora_de_estoque_db()` para obter uma lista com os nomes dos produtos que estão atualmente fora de estoque.
    Se nenhum produto estiver fora de estoque, exibe uma mensagem indicando isso e retorna uma lista vazia.
    Caso contrário, imprime um cabeçalho e lista os nomes de todos os produtos fora de estoque, retornando a lista.

    Retorna:
        list: Uma lista com os nomes dos produtos fora de estoque. Retorna uma lista vazia se nenhum for encontrado.
    """
    soldout = produtos_fora_de_estoque_db()
    if not soldout:
        print("Nenhum produto fora de estoque.")
        return []
    else:
        print("~~~~ PRODUTOS FORA DE ESTOQUE ~~~~\n")
        for nome in soldout:
            print(f"Produto: {nome}")
        return soldout
            
def iniciar_compra(id_cliente, data_compra):
    """
    Inicia uma nova compra para um cliente específico na data fornecida.

    Args:
        id_cliente (int): O identificador único do cliente que está realizando a compra.
        data_compra (str): A data da compra no formato esperado pelo banco de dados.

    Returns:
        int: O identificador único da compra criada no banco de dados.

    Efeitos Colaterais:
        Imprime no console uma mensagem indicando o início da compra com o ID e o timestamp atual.
    """
    agora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    compra_id = criar_compra_db(id_cliente, data_compra)
    print(f'Compra de ID {compra_id} iniciada em {agora}.')
    return compra_id

