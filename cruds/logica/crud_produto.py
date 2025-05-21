from cruds.operacoes_db.crud_produto_db import (
    buscar_produto_db,
    listar_produtos_db,
    atualizar_estoque_db,
)

# Interação com o usuário e tratamento de erros

def listar_produtos():
    """
    Lista todos os produtos cadastrados recuperando-os do banco de dados e imprimindo seus detalhes.
    Se nenhum produto for encontrado, exibe uma mensagem indicando que não há produtos cadastrados.

    Retorna:
        None
    """
    produtos = listar_produtos_db()
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\nProdutos cadastrados:")
        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Preço: R$ {produto[3]}")

def buscar_produto(id_produto):
    try:
        id_produto = int(id_produto)
        if id_produto <= 0:
            print("O ID do produto deve ser um número inteiro maior que zero.")
            return None
    except ValueError:
        print("O ID do produto deve ser um número inteiro.")
        return None

    produto = buscar_produto_db(id_produto)
    if not produto:
        print("Produto não encontrado.")
    return produto

def atualizar_estoque(id_produto, quantidade_vendida):
    """
    Atualiza o estoque de um produto após uma venda.
    Parâmetros:
        id_produto (int): O identificador do produto cujo estoque será atualizado.
        quantidade_vendida (int): A quantidade do produto vendida.
    Comportamento:
        - Verifica se a quantidade vendida é um inteiro maior que zero.
        - Busca o produto pelo id fornecido.
        - Verifica se há estoque suficiente para a venda.
        - Atualiza o estoque do produto no banco de dados.
        - Exibe mensagens informativas em caso de erro ou sucesso.
    Retorna:
        None
    """
    try:
        quantidade_vendida = int(quantidade_vendida)
        if quantidade_vendida <= 0:
            print("A quantidade vendida deve ser um número inteiro maior que zero.")
            return
    except ValueError:
        print("A quantidade vendida deve ser um número inteiro.")
        return

    produto = buscar_produto(id_produto)
    if not produto:
        return
    produto_id = produto[0]
    produto_nome = produto[1]
    produto_quantidade = produto[2]
    if quantidade_vendida > produto_quantidade:
        print(f'Quantidade vendida maior que a disponível para o produto {produto_nome}.')
        return
    nova_quantidade = produto_quantidade - quantidade_vendida
    atualizar_estoque_db(produto_id, nova_quantidade)
    print(f"Estoque de '{produto_nome}' atualizado para {nova_quantidade}.")
        
    