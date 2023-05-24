# Venda de Passagens Aereas

# Armazenamento de informações
d_voo = {}  # Dicionário para armazenar os voos
l_escala = []  # Lista para armazenar as cidades de escala

print(f"\n{'Seja bem vindo!':^80}")

while True:
    print("-" * 80)  # Menu inicial
    print(f'{"Menu Inicial":^80}')
    print("-" * 80)

    try:
        opc_menu = int(input(
            f" [1] - Área Cliente \n [2] - Área Interna \n [3] - Sair do Programa\n Digite a opção escolhida: "
        ))
    except ValueError:
        print("\n\tERRO: Informe apenas números!\n")
        continue

    if opc_menu == 3:  # Sair do Programa
        print("-" * 80)
        print(f"{'Obrigada! Volte Sempre!':^80}\n")
        break
    elif opc_menu == 2:  # Menu colaborador

        while True:
            print("-" * 80)
            print(f'{"Menu Interno! Seja Bem Vindo Colaborador!":^80}')
            print("-" * 80)
            print(f" [1] - Cadastrar Voo \n [2] - Alterar Informações de Voo \n [3] - Apagar voo\n [4] - "
                  f"Voltar ao menu anterior")

            try:
                opc_menu = int(input("Digite a opção escolhida: "))
            except ValueError:
                print("\n\tERRO: Informe apenas números!\n")
                continue

            if opc_menu == 4:  # Voltar ao menu anterior
                break
            elif opc_menu == 1:  # Cadastrar voo
                print("\n")
                print("-" * 80)
                print(f'{"Cadastro de Voo":^80}')
                l_escala.clear()

                while True:
                    try:
                        cod_voo = int(input("Digite o código do voo: "))
                        if cod_voo in d_voo:
                            print("Código já existente!")
                        else:
                            break
                    except ValueError:
                        print("ERRO: INSIRA SOMENTE NÚMEROS!")

                cidade_origem = input("Insira o nome da cidade de origem do voo: ").strip().upper()
                cidade_destino = input("Insira a cidade de destino do voo: ").strip().upper()

                while True:
                    try:
                        n_escalas = int(input("Insira a quantidade de escalas: "))
                        for escala in range(1, n_escalas + 1):
                            escala = input(f"Insira o nome da {escala}ª cidade de escala: ")
                            l_escala.append(escala)
                        break
                    except ValueError:
                        print("ERRO: INSIRA SOMENTE NÚMEROS!")

                d_voo[cod_voo] = [cidade_origem, cidade_destino, n_escalas, l_escala]
                print(d_voo)
                print('-' * 80)
                print(f'\n{"Voo adicionado com sucesso!":^80}\n')
                print("-" * 80)

            elif opc_menu == 2:  # Alterar informações de voo
                try:
                    cod_voo = int(input("Digite o código do voo que deseja alterar: "))
                    if cod_voo not in d_voo:
                        print("Voo não encontrado!")
                        continue
                except ValueError:
                    print("ERRO: INSIRA SOMENTE NÚMEROS!")
                    continue

                voo = d_voo[cod_voo]
                print("Informações do Voo:")
                print(f"Código Voo: {cod_voo}")
                print(f"Cidade de Origem: {voo[0]}")
                print(f"Cidade de Destino: {voo[1]}")
                print(f"Número de Escalas: {voo[2]}")
                print(f"Cidades de Escala: {voo[3]}")

                while True:
                    try:
                        n_alteracao = int(input("Escolha o item a ser alterado ou digite 0 para sair: "))
                        if n_alteracao == 0:
                            break
                        elif n_alteracao < 1 or n_alteracao > 4:
                            print("Opção inválida! Escolha um número de 1 a 4.")
                            continue
                        else:
                            if n_alteracao == 1:
                                cidade_origem = input("Insira o novo nome da cidade de origem: ").strip().upper()
                                d_voo[cod_voo][0] = cidade_origem
                                print("Cidade de origem alterada com sucesso!")
                            elif n_alteracao == 2:
                                cidade_destino = input("Insira o novo nome da cidade de destino: ").strip().upper()
                                d_voo[cod_voo][1] = cidade_destino
                                print("Cidade de destino alterada com sucesso!")
                            elif n_alteracao == 3:
                                n_escalas = int(input("Insira o novo número de escalas: "))
                                d_voo[cod_voo][2] = n_escalas
                                l_escala.clear()
                                for escala in range(1, n_escalas + 1):
                                    escala = input(f"Insira o nome da {escala}ª cidade de escala: ")
                                    l_escala.append(escala)
                                d_voo[cod_voo][3] = l_escala
                                print("Número de escalas e cidades de escala alterados com sucesso!")
                            elif n_alteracao == 4:
                                print("Cidades de escala:")
                                for i, escala in enumerate(voo[3], start=1):
                                    print(f"{i}. {escala}")
                                while True:
                                    try:
                                        n_cidade = int(input("Escolha o número da cidade de escala a ser alterada "
                                                             "ou digite 0 para sair: "))
                                        if n_cidade == 0:
                                            break
                                        elif n_cidade < 1 or n_cidade > len(voo[3]):
                                            print("Opção inválida!")
                                            continue
                                        else:
                                            nova_cidade = input("Insira o novo nome da cidade de escala: ")
                                            d_voo[cod_voo][3][n_cidade - 1] = nova_cidade
                                            print("Cidade de escala alterada com sucesso!")
                                        break
                                    except ValueError:
                                        print("ERRO: INSIRA SOMENTE NÚMEROS!")
                        break
                    except ValueError:
                        print("ERRO: INSIRA SOMENTE NÚMEROS!")

            elif opc_menu == 3:  # Apagar voo
                try:
                    cod_voo = int(input("Digite o código do voo que deseja apagar: "))
                    if cod_voo not in d_voo:
                        print("Voo não encontrado!")
                        continue
                except ValueError:
                    print("ERRO: INSIRA SOMENTE NÚMEROS!")
                    continue

                del d_voo[cod_voo]
                print(f"Voo de código {cod_voo} apagado com sucesso!")

            else:
                print("Opção inválida! Escolha um número de 1 a 3.")
