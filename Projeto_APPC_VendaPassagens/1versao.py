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

print("-"*40)
print(f"\n{'Seja bem vindo!':^40}\n")


while controle>0:

    while True:
        try:
            print("-"*40) #menu inicial
            print(f'\n{"Menu Inicial":^40}\n')
            opc_menu=int(input(f" [1] - Are Cliente \n [2] - Area Interna \n [3] - Sair do Programa\n Digite a opcao escolhida: "))
            if opc_menu>3 or opc_menu<1:
                print("\n\t!!Escolha dentre as opcoes oferecidas abaixo!!\n")

        except ValueError: 
            print("\n\tERRO: Informe apenas numeros!\n")

        if opc_menu==3: #Sair do Programa
            print("-"*40)
            print(f"{'Obrigada! Volte Sempre!':^40}\n")
            controle=0
            break
        elif opc_menu==2: #menu colaborador
            print("\n")
            print("-"*40)
            print(f'{"Seja Bem Vindo Colaborador!":^40}')
            print(f'{"Menu Interno ":^40}')
            print("-"*40)
            opc_menu=int(input(f" [1] - Cadastrar Voo \n [2] - Alterar Informacoes de Voo \n [3] - Apagar voo\n [4] - Voltar ao menu anterior\n Digite a opcao escolhida: "))
          
            if opc_menu==4: #voltar ao menu anterior
                break
            elif opc_menu ==1: #cadastrar voo
                des_continuar=1

                while des_continuar>0: #castro voo / proximo voo
                    print("\n")
                    print("-"*40)           
                    print(f'{"Castro de VOO":^40}')
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
                            elif conf_inf>4 or conf_inf<1:
                                print("OPCAO INVALIDA: Escolha dentre as opcoes disponiveis!")
                            else:
                                print( f"\nInformacoes Adicionadas: \n [1] - Codigo Voo: {cod_voo}\n [2] - Cidade de Origem: {cidade_origem}\n [3] - Cidade de Destino: {cidade_destino}\n [4] - Escalas para {l_escala}): ")
                                n_alteracao = int(input("Escolha o item a ser alterado, ou digite [5] para sair: "))
                                if n_alteracao>5 or n_alteracao<1:
                                    print("Escolha uma opcao valida!")
                                elif n_alteracao ==5: 
                                    break
                                elif n_alteracao ==1:
                                    cod_voo = int(input("Digite o codigo do voo: "))
                                elif n_alteracao ==2:
                                    cidade_origem= input("Insira o nome da cidade de origem do voo: ").strip().upper()
                                elif n_alteracao==3:
                                    cidade_destino= input("Insira a cidade de destino do voo: ").strip().upper()
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
                    print('-'*40)
                    print(f'\n\n{f"Voo {nome_voo}, adicionado com sucesso!":^40}\n\n')
                    print("-"*40)
                    #Continuacao do cadastro
                    des_continuar=int(input("\nDeseja Inserir Outro VOO?:[1] - SIM   [0] - NAO: "))
                    #em caso de 0 retorna ao menu inicial

            elif opc_menu==2:   ## alterar informacoes de voo

                des_continuar=1

                while des_continuar>0:
                    print("\n\n")
                    print("-"*80)
                    print(f"{'Seja Bem Vindo ao Sistema de Alteracao de VOO':^80}")
                    print('-'*80)

                    #voos cadastrados
                    if len(d_voo) != 0:
                        print('-' * 150)
                        print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
                        print('-' * 150)

                        for cod_voo, voo_inf in d_voo.items():
                            print(f'| {cod_voo:^10} | {str(voo_inf[1]):^20} | {str(voo_inf[2]):^30} | {str(voo_inf[3]):^22} | {str(voo_inf[4]):^22} | {str(voo_inf[5]):^33} |')

                            print('-'* 150)

                        #alteracao  
                        while True:
                            
                            try: 
                                des_continuar=int(input("Deseja Alterar Algum VOO?: [1] - SIM [2] - VOO "))

                                if des_continuar==1:
                                    cod_voo_busca=int(input("\nDigite o codigo do voo que deseja alterar: "))
                                
                            except:
                                print("Digite apenas numeros inteiros!")
                            
                            if cod_voo_busca in d_voo.keys():                                
                                cidade_origem=input("Cidade de origem: ")
                                cidade_destino=input("Cidade de destino: ")

                                while True:
                                    try:
                                        n_escalas = int(input("Insira o numero de escalas: "))
                                        break
                                    except:
                                        print("Insira apenas numeros!")
                                l_escala=[]

                                for escala in range(1,n_escalas+1):
                                    escala = input(f"Insira o nome da {escala}º cidade de escala: ")
                                    l_escala.append(escala)

                                for voo, alteracao in voo.items():
                                    if voo==cod_voo_busca:
                                        alteracao[1]=cidade_origem
                                        alteracao[2]=cidade_destino
                                        alteracao[3]=n_escalas
                                        alteracao[4]=l_escala
                                        print("\n Alteracoes realizadas com sucesso!\n")
                                break
                            else:
                                print("\n ERRO: ESTE VOO NAO EXISTE!")
                    elif d_voo=={}:
                        print("Nenhum voo cadastrado!")
                        break
                    else:
                        print("\n VOO nao cadastrado!")
                        break