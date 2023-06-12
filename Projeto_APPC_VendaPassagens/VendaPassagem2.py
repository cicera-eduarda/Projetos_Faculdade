# Venda de Passagens Aéreas

# Armazenamento de informações
d_voo = {}


def exibir_menu():
    print("-" * 80)
    print(f'{"Seja bem-vindo!":^80}')
    print("-" * 80)
    print("[1] - Área Cliente")
    print("[2] - Área Colaborador")
    print("[3] - Sair do Programa")


def exibir_menu_colaborador():
    print("-" * 80)
    print(f'{"Área Colaborador":^80}')
    print("-" * 80)
    print("[1] - Cadastrar Voo")
    print("[2] - Alterar Informações de Voo")
    print("[3] - Apagar Voo")
    print("[4] - Voltar ao Menu Anterior")


def exibir_menu_cliente():
    print("-" * 80)
    print(f'{"Área Cliente":^80}')
    print("-" * 80)
    print("[1] - Consultar Voo")
    print("[2] - Voltar ao Menu Anterior")


def cadastrar_voo():
    print("-" * 80)
    print(f'{"Cadastro de Voo":^80}')
    print("-" * 80)

    while True:
        cod_voo = input("Digite o código do voo: ")

        if cod_voo in d_voo:
            print("Código já existente! Digite outro código.")
        else:
            break

    cidade_origem = input("Insira o nome da cidade de origem do voo: ")
    cidade_destino = input("Insira o nome da cidade de destino do voo: ")
    num_escalas = int(input("Insira o número de escalas: "))

    escalas = []
    for i in range(num_escalas):
        escala = input(f"Insira o nome da {i + 1}ª cidade de escala: ")
        escalas.append(escala)

    d_voo[cod_voo] = {
        "Origem": cidade_origem,
        "Destino": cidade_destino,
        "Escalas": escalas
    }

    print("Voo cadastrado com sucesso!")


def alterar_voo():
    print("-" * 80)
    print(f'{"Alteração de Voo":^80}')
    print("-" * 80)

    cod_voo = input("Digite o código do voo que deseja alterar: ")

    if cod_voo in d_voo:
        print(f"Voo encontrado! Informe as novas informações:")
        cidade_origem = input("Insira o nome da cidade de origem do voo: ")
        cidade_destino = input("Insira o nome da cidade de destino do voo: ")
        num_escalas = int(input("Insira o número de escalas: "))

        escalas = []
        for i in range(num_escalas):
            escala = input(f"Insira o nome da {i + 1}ª cidade de escala: ")
            escalas.append(escala)

        d_voo[cod_voo] = {
            "Origem": cidade_origem,
            "Destino": cidade_destino,
            "Escalas": escalas
        }

        print("Voo alterado com sucesso!")
    else:
        print("Voo não encontrado!")


def apagar_voo():
    print("-" * 80)
    print(f'{"Remoção de Voo":^80}')
    print("-" * 80)

    cod_voo = input("Digite o código do voo que deseja apagar: ")

    if cod_voo in d_voo:
        del d_voo[cod_voo]
        print("Voo removido com sucesso!")
    else:
        print("Voo não encontrado!")


def consultar_voo():
    print("-" * 80)
    print(f'{"Consulta de Voo":^80}')
    print("-" * 80)

    cod_voo = input("Digite o código do voo que deseja consultar: ")

    if cod_voo in d_voo:
        print("-" * 80)
        print(f'{"Informações do Voo":^80}')
        print("-" * 80)

        print(f"Código do Voo: {cod_voo}")
        print(f"Cidade de Origem: {d_voo[cod_voo]['Origem']}")
        print(f"Cidade de Destino: {d_voo[cod_voo]['Destino']}")
        print("Escalas:")
        for i, escala in enumerate(d_voo[cod_voo]['Escalas'], 1):
            print(f"{i}. {escala}")
    else:
        print("Voo não encontrado!")


while True:
    exibir_menu()

    try:
        opc_menu = int(input("Digite a opção escolhida: "))
    except ValueError:
        print("ERRO: Informe apenas números!")
        continue

    if opc_menu == 3:
        print("-" * 80)
        print(f'{"Obrigado! Volte Sempre!":^80}')
        break

    elif opc_menu == 2:
        while True:
            exibir_menu_colaborador()

            try:
                opc_menu_colab = int(input("Digite a opção escolhida: "))
            except ValueError:
                print("ERRO: Informe apenas números!")
                continue

            if opc_menu_colab == 4:
                break

            elif opc_menu_colab == 1:
                cadastrar_voo()

            elif opc_menu_colab == 2:
                alterar_voo()

            elif opc_menu_colab == 3:
                apagar_voo()

            else:
                print("Opção inválida!")

    elif opc_menu == 1:
        while True:
            exibir_menu_cliente()

            try:
                opc_menu_cliente = int(input("Digite a opção escolhida: "))
            except ValueError:
                print("ERRO: Informe apenas números!")
                continue

            if opc_menu_cliente == 2:
                break

            elif opc_menu_cliente == 1:
                consultar_voo()

            else:
                print("Opção inválida!")

    else:
        print("Opção inválida!")

