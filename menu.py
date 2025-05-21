from caixa.abrir_caixa import abrir_caixa
from caixa.fechar_caixa import fechar_caixa
from caixa.atendimento import menu_atendimento
from utilidades.resetar_bd import resetar_banco

from caixa.abrir_caixa import abrir_caixa

def menu_principal():
    """
    Exibe o menu principal do sistema de caixa do supermercado e gerencia o fluxo de operações.
    Permite ao usuário:
    - Abrir o caixa
    - Realizar atendimentos
    - Fechar o caixa
    - Resetar o banco de dados
    - Sair do sistema
    O menu permanece em execução até que o usuário escolha sair, garantindo que o caixa esteja fechado antes de encerrar o programa.
    """
    caixa_aberto = False

    while True:
        print("\n~~~~~~~~~~~~~~~~~~~~~ KAIÁ SUPERMERDADOS  ~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~ SISTEMA DE CAIXA ~~~~~~~~~~~~~~~~~~~~~~~~")
        print('1. Abrir Caixa')
        print('2. Atendimento')
        print('3. Fechar Caixa')
        print('4. Resetar o bando de dados')
        print('0. Sair')
        print('\n')

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            abrir_caixa()
            caixa_aberto = abrir_caixa()
            print('Caixa aberto!')
            continue

        elif opcao == '2':
            if not caixa_aberto:
                print("Erro: Abra o caixa primeiro.")
            else:
                menu_atendimento()

        elif opcao == '3':
            if not caixa_aberto:
                print("Erro: Abra o caixa primeiro.")
            else:
                fechar_caixa()
                caixa_aberto = False
        
        elif opcao == '4':
            resetar_banco()

        elif opcao == '0':
            if caixa_aberto:
                print("Erro: Feche o caixa antes de sair.")
            else:
                fechar_caixa()
                print('Tschüssikowski!\n')
                break

        else:
            print("Opção inválida.")
