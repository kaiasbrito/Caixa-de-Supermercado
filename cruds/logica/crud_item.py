from tabulate import tabulate
from datetime import datetime
from cruds.operacoes_db.crud_item_db import listar_itens_por_compra_db, inserir_item 
from cruds.operacoes_db.crud_compra_db import buscar_compra_db
from cruds.operacoes_db.crud_cliente_db import buscar_cliente_db
from cruds.logica.crud_produto import buscar_produto
from cruds.logica.crud_produto import atualizar_estoque

def adicionar_item(id_compra):
    """
    Adiciona um item a uma compra existente, solicitando ao usuário o ID do produto e a quantidade desejada.
    Parâmetros:
        id_compra (int): O identificador da compra à qual o item será adicionado.
    Fluxo:
        - Solicita ao usuário o ID do produto e a quantidade desejada.
        - Verifica se o produto existe e se há estoque suficiente.
        - Insere o item na compra e atualiza o estoque do produto.
        - Exibe mensagens de sucesso ou erro conforme necessário.
    Exceções:
        ValueError: Caso o usuário forneça entradas inválidas (não inteiras).
        Exception: Para outros erros inesperados durante o processo.
    """
    print("\n~~~~ Adicionar Item à Compra ~~~~")
    
    try:
        # Solicita o ID do produto
        id_produto = int(input("Digite o ID do produto: "))
        
        # Solicita a quantidade desejada
        quantidade = int(input("Digite a quantidade desejada: "))
        
        # Verifica o estoque disponível
        produto = buscar_produto(id_produto)
        if not produto:
            print("Produto não encontrado.")
            return

        estoque_disponivel = produto[2]  # Supondo que a quantidade disponível esteja no índice 2
        if quantidade > estoque_disponivel:
            print(f"A quantidade solicitada ({quantidade}) é maior que o estoque disponível ({estoque_disponivel}).")
            return
        
        # Insere o item na tabela de compras
        inserir_item(quantidade, id_compra, id_produto)  # Verifique que o banco está sendo atualizado corretamente aqui
        
        # Atualiza o estoque do produto
        atualizar_estoque(id_produto, quantidade)  # Chama a função de atualização de estoque
        
        agora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"Produto {id_produto} adicionado à compra {id_compra} às {agora}.\n")
    
    except ValueError:
        print("Entrada inválida. Use apenas números inteiros para ID e quantidade.\n")
    except Exception as e:
        print(f"Erro ao inserir item: {e}\n")



def gerar_nota_fiscal(id_compra):
    """
    Gera e exibe a nota fiscal de uma compra específica.
    Parâmetros:
        id_compra (int): O identificador da compra para a qual a nota fiscal será gerada.
    Fluxo:
        - Busca a compra pelo ID informado.
        - Caso não exista, exibe mensagem de erro e retorna.
        - Recupera o cliente e a data da compra.
        - Lista os itens associados à compra.
        - Caso não existam itens, exibe mensagem de erro e retorna.
        - Calcula o subtotal de cada item e o total da compra.
        - Exibe a nota fiscal formatada, incluindo cliente, data, itens, quantidade, preço, subtotal e total.
    Dependências:
        - Funções auxiliares: buscar_compra_db, buscar_cliente_db, listar_itens_por_compra_db.
        - Biblioteca: tabulate (para exibição em tabela).
    """
    compra = buscar_compra_db(id_compra)
    if not compra:
        print('Não existem compras com esse ID.')
        return
    id_cliente, data_compra = compra
    
    nome_cliente = buscar_cliente_db(id_cliente)
    
    itens = listar_itens_por_compra_db(id_compra)
    if not itens:
        print('Não há itens registrados nessa compra.')
        return
    
    tabela = []
    total = 0
    
    for i, (nome_produto, quantidade, preco) in enumerate(itens, start=1):
        subtotal = quantidade * preco
        total += subtotal
        tabela.append([i, nome_produto, quantidade, preco, subtotal])

    print("~~~~~~ Nota fiscal ~~~~~~\n")
    print(f"Cliente {id_cliente} - {nome_cliente}")
    print(f"Data: {data_compra}\n")
    print(tabulate(tabela, headers=["Item", "Produto", "Quantidade", "Preço", "Subtotal"], tablefmt="grid"))
    print(f"\nItens: {len(itens)}")
    print(f"Total: {total}")
        
