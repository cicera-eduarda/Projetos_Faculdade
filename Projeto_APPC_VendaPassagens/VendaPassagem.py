## Cicera Eduarda da Costa 23016727
#Venda de Passagens Aereas


#Armazenamento de informaçĩes
    #Codigo do Voo (Chave do dicionario)
d_voo={}
cid_origem=''
cid_destino=''
l_escala=[] #cidades para escala
#Cidade de Origem
#Cidade de Destino
#Numero de Escalas
#Cidades da Escala, quando houver escalas

#Inclusao de quantos voo o usuario desejar (codigo)
#alterar informacoes sobre voo
#apagar um voo
#apartir da cidade de origem determinar quantos voo saem dessa cidadde
#origem e destino, determinar o voo com menor numero de escalas e imprimir o voo

controle=1

print(f"\n{'Seja bem vindo!':^80}")


while controle>0:

    while True:
        try:
            print("-"*80) #menu inicial
            print(f'{"Menu Inicial":^80}')
            print("-"*80) 

            opc_menu=int(input(f" [1] - Are Cliente \n [2] - Area Interna \n [3] - Sair do Programa\n Digite a opcao escolhida: "))
            if opc_menu>3 or opc_menu<1:
                print("\n\t!!Escolha dentre as opcoes oferecidas abaixo!!\n")

        except ValueError: 
            print("\n\tERRO: Informe apenas numeros!\n")
        if opc_menu==3: #Sair do Programa
            print("-"*80)
            print(f"{'Obrigada! Volte Sempre!':^80}\n")
            controle=0
            break
        elif opc_menu==2: #menu colaborador
            print("-"*80)
            print(f'{"Menu Interno! Seja Bem Vindo Colaborador!":^80}')
            print("-"*80)

            opc_menu=int(input(f" [1] - Cadastrar Voo \n [2] - Alterar Informacoes de Voo \n [3] - Apagar voo\n [4] - Voltar ao menu anterior\n Digite a opcao escolhida: "))
          
            if opc_menu==4: #voltar ao menu anterior
                break
            elif opc_menu ==1: #cadastrar voo
                des_continuar=1

                while des_continuar==1: #castro voo / proximo voo
                    print("\n")
                    print("-"*80)           
                    print(f'{"Castro de VOO":^80}')
                    l_escala=[]
                    #COD_VOO
                    while True:
                        try:
                            cod_voo = int(input("Digite o codigo do voo: "))
                            if cod_voo in d_voo.keys():
                                print(f"Codigo ja existente!")
                            else:
                                break

                        except:
                            print("ERRO: INSIRA SOMENTE NUMEROS!")

                    #CIDADE DE ORIGEM/DESTINO/NUMERO ESCALAS

                    cidade_origem= input("Insira o nome da cidade de origem do voo: ").strip().upper()
                    cidade_destino= input("Insira a cidade de destino do voo: ").strip().upper()
                    nome_voo=cidade_origem+'/'+cidade_destino
                    while True:
                        try:
                            n_escalas= int(input("Insira a quantidade de escalas: "))
                            for escala in range(1,n_escalas+1):
                                escala = input(f"Insira o nome da {escala}º cidade de escala: ")
                                l_escala.append(escala)
                            
                            break
                        except:
                            print("ERRO: INSIRA SOMENTE NUMEROS!")

                    #Conferencia informacoes
                    while True:
                        try:
                            print( f"\nInformacoes Adicionadas: \n [1] - Codigo Voo: {cod_voo}\n [2] - Cidade de Origem: {cidade_origem}\n [3] - Cidade de Destino: {cidade_destino}") 
                            if l_escala!=[]: print(f" [4] - Escalas para {l_escala})\n")
                            conf_inf= int(input("As informacoes estao corretas? [1-SIM] OU [2-NAO]: "))
                            
                            if conf_inf == 1:
                                break
                            elif conf_inf>4 or conf_inf<1: #VALIDACAO
                                print("OPCAO INVALIDA: Escolha dentre as opcoes disponiveis!")
                            else:
                                print('-'*80)
                                print( f"\n [1] - Codigo Voo: {cod_voo}\n [2] - Cidade de Origem: {cidade_origem}\n [3] - Cidade de Destino: {cidade_destino}\n [4] - Escalas para {l_escala}): ")
                                n_alteracao = int(input("Escolha o item a ser alterado, ou digite [5] para sair: "))
                                if n_alteracao>5 or n_alteracao<1:
                                    print("Escolha uma opcao valida!")
                                elif n_alteracao ==5: 
                                    break
                                elif n_alteracao ==1:
                                    cod_voo = int(input("Digite o codigo do voo: "))
                                elif n_alteracao ==2:
                                    cidade_origem= input("Insira o nome da cidade de origem do voo: ").strip().upper()
                                    nome_voo=cidade_origem+'/'+cidade_destino

                                elif n_alteracao==3:
                                    cidade_destino= input("Insira a cidade de destino do voo: ").strip().upper()
                                    nome_voo=cidade_origem+'/'+cidade_destino

                                elif n_alteracao==4:
                                    escalas= int(input("Insira a quantidade de escalas: "))
                                    for escala in range(1,escalas+1):
                                            escala = input(f"Insira o nome da {escala}º cidade de escala: ")
                                            l_escala.append(escala)
                        except ValueError:
                            print("Insira apenas numeros inteiros")

                    #Adicionando dicionarios
                    d_voo[cod_voo] = [nome_voo,cidade_origem,cidade_destino,n_escalas,l_escala]
                    print(d_voo)
                    print('-'*80)
                    print(f'\n\n{f"Voo {nome_voo}, adicionado com sucesso!":^80}\n\n')
                    print("-"*80)
                    #Continuacao do cadastro
                    
                    while True:

                        try:
                            
                            continuar=int(input("\nDeseja Inserir Outro VOO?:[1] - SIM   [2] - NAO: "))

                        except ValueError:

                            print("Insira somente numeros!")

                        if continuar>2 or continuar<1:
                            print('\nEscolha somente dentre as opçoes desejadas ')

                        else:

                            des_continuar=0
                            break

                    

                        
                    

                        



                        
                    #em caso de 0 retorna ao menu inicial

            
            elif opc_menu == 2:  # alterar informações de voo

                des_continuar = 1
                print(f"{'Seja Bem Vindo ao Sistema de Alteração de VOO':^150}")

                while des_continuar > 0:
                    print("\n\n")
                    print("-" * 150)
                    print('-' * 150)

                    # voos cadastrados
                    if len(d_voo) != 0:
                        print('-' * 150)
                        print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
                        print('-' * 150)

                        for cod_voo, voo_inf in d_voo.items():
                            print(f'| {cod_voo:^10} | {str(voo_inf[0]):^20} | {str(voo_inf[1]):^30} | {str(voo_inf[2]):^20} | {str(voo_inf[3]):^20} | {str(voo_inf[4]):^32} |')

                            print('-' * 150)

                        # alteração
                        while True:

                            try:
                                des_continuar = int(input("Deseja Alterar Algum VOO?: [1] - SIM    [2] - NÃO: "))


                                if des_continuar == 1:
                                    cod_voo_busca = int(input("\nDigite o código do voo que deseja alterar: "))

                                    if cod_voo_busca in d_voo.keys():
                                        voo_inf = d_voo[cod_voo_busca]

                                        cidade_origem = input("Cidade de origem: ")
                                        cidade_destino = input("Cidade de destino: ")
                                        nome_voo= cidade_origem+'/'+cidade_destino
                                        while True:
                                            try:
                                                n_escalas = int(input("Insira o número de escalas: "))
                                                break
                                            except:
                                                print("Insira apenas números!")

                                        l_escala = []

                                        for escala in range(1, n_escalas + 1):
                                            escala = input(f"Insira o nome da {escala}ª cidade de escala: ")
                                            l_escala.append(escala)
                                        voo_inf[0] = nome_voo
                                        voo_inf[1] = cidade_origem
                                        voo_inf[2] = cidade_destino
                                        voo_inf[3] = n_escalas
                                        voo_inf[4] = l_escala

                                        print("\nAlterações realizadas com sucesso!")
                                        print("Confira abaixo a tabela de atualizacao dos voos!")
                                        break
                                    else:
                                        print("\nERRO: Este voo não existe!")
                                        break
                                elif des_continuar==2:
                                    print("Voltando ao menu principal!")
                                    break
                                else:
                                    print(f"{'Digite uma opcao valida!':^80}")

                            except ValueError:
                                print("Digite apenas números inteiros!")

                    else:
                        print("Nenhum voo cadastrado!")
                        break

            elif opc_menu==3: #exclusao por colaborador
                print('-'*80)
                print(f"{'Seja Bem Vindo ao Sistema de Exclusao de VOO':^80}")


                if d_voo==[]:

                    des_continuar=1
                    while des_continuar==1:
                        # voos cadastrados
                        if len(d_voo) != 0:
                            print('-' * 150)
                            print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
                            print('-' * 150)

                            for cod_voo, voo_inf in d_voo.items():
                                print(f'| {cod_voo:^10} | {str(voo_inf[0]):^20} | {str(voo_inf[1]):^30} | {str(voo_inf[2]):^20} | {str(voo_inf[3]):^20} | {str(voo_inf[4]):^32} |')

                                print('-' * 150)

                            # Exclusao
                            while True:

                                try:
                                    des_continuar = int(input("Deseja Excluir Algum VOO?: [1] - SIM    [2] - NÃO: "))


                                    if des_continuar == 1:
                                        cod_voo_busca = int(input("\nDigite o código do voo que deseja excluir: "))
                                    else:
                                        break
                                except ValueError:
                                    print("Digite apenas números inteiros!")

                                if cod_voo_busca in d_voo.keys():
                                    d_voo.pop(cod_voo_busca)
                                    print("\nVoo EXCLUIDO COM SUCESSO")
                                    break
                        else:
                            break
                else:
                    print(f'\n{"Nenhum Voo Encontrado! Voce Sera Redirecionado ao Menu Principal!":^80}')     

        elif opc_menu==1: #menu cliente

            while True: #laco menu cliente para gerar laço

                print("-"*80)
                print(f"{'Bem Vindo Cliente!':^80}")
                print("-"*80)
                try: 
                    opc_menu=int(input(f" [1] - Buscar VOO por: Origem \n [2] - Buscar Voo por: Origem e Destino \n [3] - Voltar ao menu anterior\n Digite a opcao escolhida: "))

                except ValueError:
                    print("\nERRO: Apenas Numeros!")
                if opc_menu<1 or opc_menu>3:
                    print("\nOpcao invalida!")
                elif opc_menu==3:
                    break
                elif opc_menu==1:
                    print("-"*80)
                    print(f"{'Busca por Cidade de Origem!':^80}")
                    print("-"*80)
                    while True:
                        nome_origem=input("Digite o nome da cidade de origem: ").strip().upper()
                        c = 0
                        for codigo, cidade in d_voo.items():
                            if cidade[1]==nome_origem:
                                print(f'\n{"|| VOOS DISPONIVEIS PARA: {nome_origem} ||":^150}')

                                print('-' * 150)
                                print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
                                print('-' * 150)

                                print(f'| {cod_voo:^10} | {str(voo_inf[0]):^20} | {str(voo_inf[1]):^30} | {str(voo_inf[2]):^20} | {str(voo_inf[3]):^20} | {str(voo_inf[4]):^32} |')

                                print('-' * 150)


            

