from cruds.logica.crud_cliente import buscar_cliente, cadastrar_cliente
from cruds.logica.crud_compra  import iniciar_compra
from cruds.logica.crud_item import gerar_nota_fiscal, adicionar_item
from datetime import datetime

def menu_atendimento():
    id_compra = None

    # Verifica o cliente
    id_cliente = input("Digite o ID do cliente: ")
    cliente = buscar_cliente(id_cliente)
    if not cliente:
        print("Cliente não encontrado. Vamos cadastrar um novo.")
        cadastrar_cliente()
        cliente = buscar_cliente(id_cliente)
        if not cliente:
            print("Erro ao cadastrar cliente. Abortando atendimento.\n")
            return

    id_cliente = cliente[0][0]  # Dados do cliente

    print(f"\n=== ATENDIMENTO INICIADO ===")
    agora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    id_compra = iniciar_compra(id_cliente, agora)

    # 2) Loop de produtos
    while True:
        print("1. Adicionar produto")
        print("2. Finalizar atendimento")
        print("0. Cancelar atendimento")
        opcao = input("Opção: ")

        if opcao == '1':
            # Chama a função de adicionar item que agora já inclui a atualização do estoque
            produto_valido = adicionar_item(id_compra)
            if produto_valido:
                pass

        elif opcao == '2':
            print('')
            gerar_nota_fiscal(id_compra)
            print("Atendimento finalizado.\n")
            break

        elif opcao == '0':
            print("Atendimento cancelado.\n")
            break

        else:
            print("Opção inválida. Digite 1, 2 ou 0.\n")