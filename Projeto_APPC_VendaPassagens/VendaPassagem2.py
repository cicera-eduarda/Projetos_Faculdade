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
    print("[1] - Buscar VOO por Origem: ")
    print("[2] - Buscar VOO por Origem e Destino: ")
    print("[3] - Voltar ao Menu Anterior: ")


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

    cidade_origem = input("Insira o nome da cidade de origem do voo: ").strip().upper()
    cidade_destino = input("Insira o nome da cidade de destino do voo: ").strip().upper()
    num_escalas = int(input("Insira o número de escalas: "))

    escalas = []
    for i in range(num_escalas):
        escala = input(f"Insira o nome da {i + 1}ª cidade de escala: ").strip().upper()
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

    cod_voo = input("Digite o código do voo que deseja alterar: ").strip().upper()

    if cod_voo in d_voo:
        print(f"Voo encontrado! Informe as novas informações:")
        cidade_origem = input("Insira o nome da cidade de origem do voo: ").strip().upper()
        cidade_destino = input("Insira o nome da cidade de destino do voo: ").strip().upper()
        num_escalas = int(input("Insira o número de escalas: "))

        escalas = []
        for i in range(num_escalas):
            escala = input(f"Insira o nome da {i + 1}ª cidade de escala: ").strip().upper()
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

    cod_voo = input("Digite o código do voo que deseja apagar: ").strip().upper()

    if cod_voo in d_voo:
        del d_voo[cod_voo]
        print("Voo removido com sucesso!")
    else:
        print("Voo não encontrado!")


def consultar_voo(): # cidade de origem
    print("-" * 80)
    print(f'{"Consulta de Voo por Origem":^80}')
    print("-" * 80)

    while True:
        nome_origem = input("Digite o nome da cidade de origem: ").strip().upper()
        c = 0
        print(f'\n|{f"VOOS DISPONIVEIS PARA: {nome_origem}":^149}|')
        print('-' * 150)
        print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
        print('-' * 150)

        for codigo, cidade in d_voo.items():
            if cidade[1] == nome_origem:
                print(f'| {codigo:^10} | {str(cidade[0]):^20} | {str(cidade[1]):^30} | {str(cidade[2]):^20} | {str(cidade[3]):^20} | {str(cidade[4]):^32} |')
                print('-' * 150)
                c = 1
        if c == 0:
            print(f"|{f'Sem Voo Disponiveis! Para a cidade {nome_origem}':^150}|")

        buscar_novamente = int(input("Deseja buscar outra cidade? [1] - Sim  [2] - Nao: "))
        if buscar_novamente == 2:
            break
        else:
            print("")


def consultar_voo_cidades(): #cidade origem/destino
    print("-" * 80)
    print(f"{'Busca por Cidade de Origem!':^80}")
    print("-" * 80)

    while True:
        cidade_origem = input("Insira o nome da cidade de ORIGEM: ").strip().upper()
        cidade_destino = input("Insira o nome da cidade de DESTINO: ").strip().upper()
        l_escala = []
        C = 0
        
        for cid, cidade in d_voo.items():
            if cidade[1] == cidade_origem and cidade[2] == cidade_destino:
                l_escala.append(cidade[3])
            
            elif cidade[1] != cidade_origem or cidade[2] != cidade_destino:
                C = 1
        
        if C == 0:
            print("Nenhum voo cadastrado nesta origem!")
        
        if len(l_escala) > 0:
            menor_escala = min(l_escala)
            
            for cid, cidade in d_voo.items():
                if cidade[3] == menor_escala:
                    if cidade[1] == cidade_origem and cidade[2] == cidade_destino:
                        voo = d_voo[cid]
                        
                        print(f'\n{f"|| VOOS DISPONIVEIS COM MENOR ESCALA: {cidade_origem} ||":^150}')
                        print('-' * 150)
                        print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
                        print('-' * 150)
                        print(f'| {cid:^10} | {str(voo[0]):^20} | {str(voo[1]):^30} | {str(voo[2]):^20} | {str(voo[3]):^20} | {str(voo[4]):^32} |')
                        print('-' * 150)
        deseja_continuar=int(input("Deseja realizar outra busca? [1] - SIM   [2] - NAO : "))
        if deseja_continuar==1:
            print("Realize outra busca!")
        else:
            print('')
            break

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

            if opc_menu_cliente == 3:
                break

            elif opc_menu_cliente == 1: #busca por cidade
                consultar_voo()
            elif opc_menu_cliente == 2: #busca por cid_orig/cid_destino
                consultar_voo_cidades()
            else:
                print("Opção inválida!")

    else:
        print("Opção inválida!")

