#Ferramentas

d_livros={}
l_autores=[]
print('Sistema de Livraria')


#Sistema de cadastro e Sistema de busca
while True:

    while True:
        try:
            escolha_sistema = int(input("Escolha entre as opcoes abaixo:\n 1 - Cadastrar livros \n 2 - Buscar livros \n 3 - Sair \n Digite a opção escolhida: "))
            break
        except ValueError:
            print("\n\nDigite somente numeros!\n\n")

    if escolha_sistema<1 or escolha_sistema>3:
        print("\nEscolha um opçaõ valida!\n") 
    else:
        break
           
# Escolha do sistema 

while 1<=escolha_sistema<=3:

    ##Sai do sistema 
  
    if escolha_sistema ==3:
        print("Volte sempre!")
        break

    #Sistema de Castro
    if escolha_sistema ==1:
        print("\n\n\tSistema de Cadastro")

        deseja_continuar=1
        contador = 0

        while deseja_continuar==1:
            contador+=1

            #Entrada e validacao codigo_livro
            while True: 
                try:
                    codigo_livro= int(input(f"\nDigite o codigo do livro {contador}: "))
                    break

                except ValueError:
                    print("Digite uma entrada valida! Apenas numeros inteiros")

            ##Busca do codigo para ver se o mesmo já existe
            if codigo_livro in d_livros.keys():
                print(f"Codigo ja existente! Pertence ao livro {d_livros[0]}")
                codigo_livro= int(input(f"Digite novamente o codigo do livro {contador}: "))

            #Entrada nome do livro
            titulo_livro = input(f"Digite o nome do livro {contador}: ").upper()

            #Entrada numero de autores
            while True:
                try:
                    n_autores = int(input(f"Digite o numero de autores do livro {contador}: "))
                    break

                except ValueError:
                    print("Digite apenas numeros!")
            
            for autor in range(1,n_autores+1):
                autor=input(f"Digite nome do {autor}º autor do livro {contador}: ")
                l_autores.append(autor)
            
            #Preco
            preco_livro= float(input(f"Insira o valor do preco do livro {contador}: "))

            #Conferencia de informacoes

            while True:
                try:
                    print(f"Informacoes adicionadas: \n 1- Codio Livro: {codigo_livro} \n 2- Titulo: {titulo_livro} \n 3- Numero de Autores: {n_autores} \n 4- Nome Autores: {l_autores} \n 5 -Preco: {preco_livro}")
                    conf_informacoes = int(input(f"As informações estao corretas? [1-SIM] ou [2-NAO]: "))
                   
                    if conf_informacoes == 1:
                        break
                    elif conf_informacoes > 6 or conf_informacoes< 1:
                        print("Escolha uma opçao valida!")
                    else:
                        n_alteracao = int(input("Escolha o item para ser alterada ou [6]- Para sair : "))
                        if n_alteracao==6:
                            break
                        elif n_alteracao ==1:
                            codigo_livro=int(input("Insira o codigo do livro correto: "))
                        elif n_alteracao ==2:
                            titulo_livro= input("Digite o titulo correto do livro: ")
                        elif n_alteracao ==3:
                            n_autores = int(input("Digite o numero de autores correto: "))
                        elif n_alteracao==4:
                            for autor in range(1,n_autores+1):
                                autor=input(f"Digite nome do {autor}º autor: ")
                                l_autores.append(autor)
                        elif n_alteracao ==5:
                            preco_livro= float(input(f"Insira o preco do livro {contador}, correto: "))
                except ValueError:
                    print("Insira apenas numeros inteiros!")
            
             #Adicao dicionario
            d_livros[codigo_livro]=[titulo_livro,n_autores,l_autores]
            print(f"Livro adicionado com sucesso! {d_livros}")
            
            #Continuacao Cadastro

            deseja_continuar=(input("Deseja Inserir outro livro?: [1-Sim / 2-Nao]: "))

            #Proximo programa colocar em laco antes de tudo
            if deseja_continuar==2:
                while True:
                    while True:
                        try:
                            escolha_sistema = int(input("Escolha entre as opcoes abaixo:\n 1 - Cadastrar livros \n 2 - Buscar livros \n 3 - Sair \n Digite a opção escolhida: "))
                            break
                        except ValueError:
                            print("\n\nDigite somente numeros!\n\n")

                    if escolha_sistema<1 or escolha_sistema>3:
                        print("\nEscolha uma opçaõ valida!\n") 
                    else:
                        break
            


     #Sistema de Busca

    if escolha_sistema==2:

        print("\n\n \t Sistema de Busca! ")
        print(f"Livros cadastrados no Sistema {contador}")

        #Escolha do tipo de busca desejado

        while True:

            while True:
                try:
                    busca=input(f"Deseja buscar por: [1] - Titulo [2] - Codigo [3] - Sair")
                    break
                except ValueError:
                    print("Digite apenas numeros!")
            if busca<1 or busca>3:
                print("Escolha uma opcao valida!")
                
            else:
                break
        
        


        busca_titulo=input("Digite o nome do livro para Busca: ").upper().trim()


        #Deseja buscar novamente outro livro?
           

            




#Entrada de dados representando de um livro



