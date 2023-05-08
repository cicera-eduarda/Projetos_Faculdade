#Ferramentas

d_livros={}
l_autores=[]
print('Sistema de Livraria')


#Sistema de cadastro e Sistema de busca

while True:
    try:
        escolha_sistema = int(input("Escolha entre as opcoes abaixo:\n 1 - Cadastrar livros \n 2 - Buscar livros \n 3 - Sair \n Digite a opção escolhida: "))
        break

    except ValueError:
        print("\n\nDigite somente numeros!\n\n")
    
if escolha_sistema<1 or escolha_sistema>3:
    print("Escolha um opçaõ valida!")

while 1<=escolha_sistema<=3:

##Sistema de Cadastros 

    
    if escolha_sistema ==3:
        print("Volte sempre!")
        break

    #Sistema de Castro
    if escolha_sistema ==1:
        print("\n\n\tSistema de Cadastro")

        deseja_continuar=1
        contador = 1

        while deseja_continuar==1:

            #Entrada e validacao codigo_livro
            while True: 
                try:
                    codigo_livro= int(input(f"\nDigite o codigo do livro {contador}: "))
                    break

                except ValueError:
                    print("Digite uma entrada valida! Apenas numeros inteiros")

            #Entrada nome do livro
            titulo_livro = input("Digite o nome do livro: ").upper()

            #Entrada numero de autores
            while True:
                try:
                    n_autores = int(input("Digite o numero de autores: "))
                    break

                except ValueError:
                    print("Digite apenas numeros!")
            
            for autor in range(1,n_autores+1):
                autor=input(f"Digite nome do {autor}º autor: ")
                l_autores.append(autor)

        #Adicao dicionario
        d_livros[codigo_livro]=[titulo_livro,n_autores,l_autores]
        print(d_livros)
            





#Entrada de dados representando de um livro



