from datetime import datetime
from tabulate import tabulate
from cruds.operacoes_db.crud_compra_db import total_vendas_db
from cruds.logica.crud_compra import vendas_por_cliente, produtos_fora_de_estoque
from utilidades.config import DB_PATH


def fechar_caixa():
    """
    Fecha o caixa do supermercado, exibindo um resumo das vendas do dia.
    Esta função realiza as seguintes operações:
    - Obtém as vendas agrupadas por cliente.
    - Calcula o total geral de vendas do dia.
    - Exibe a data e hora do fechamento.
    - Mostra o status do estoque antes do fechamento.
    - Exibe uma tabela com o resumo das vendas por cliente, incluindo quantidade de itens e valor total.
    - Mostra o total geral de vendas do dia.
    Se não houver vendas registradas, informa ao usuário e encerra a execução.
    Requer:
        - As funções auxiliares: vendas_por_cliente(), total_vendas_db(), produtos_fora_de_estoque().
        - O módulo datetime.
        - O módulo tabulate.
    Não recebe parâmetros.
    Não retorna valores.
    """
    compras = vendas_por_cliente()
    total_geral = total_vendas_db()

    # Verificando se há vendas para exibir
    if not compras:
        print("Nenhuma venda registrada.")
        return

    print("\nFechamento do caixa")
    print("Data:", datetime.now().strftime("%d/%m/%Y %H:%M"))

    # Status do estoque antes do fechamento
    print("\nStatus do Estoque:")
    produtos_fora_de_estoque()

    # Monta a tabela com id_cliente, total_itens e total_valor
    tabela = [
        [f"Cliente {c[0]} — {c[1]}", c[2], f"R$ {c[3]:.2f}"]
        for c in compras
    ]
    print()
    print(tabulate(
        tabela,
        headers=["Cliente", "Quantidade Vendida", "Total (R$)"],
        tablefmt="grid"
    ))

    # Exibe o total geral
    if total_geral > 0:
        print(f"\nTotal de vendas no dia: R$ {total_geral:.2f}\n")
    else:
        print("\nNenhuma venda registrada no total.\n")