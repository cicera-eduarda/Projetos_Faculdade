#Entrada de informacoes
print('Sistema de livraria')
dic = {}
n=1
conf = 0
while n == 1:

    opc = int(input('digite 1 para cadastrar um livro, 2 para buscar e 3 para sair: '))

    if opc < 1 or opc > 3:
        print("Opcao invalida, escolha uma disponivel!")
    elif opc == 1:
        while conf == 0:
            lista = []
            lista_autores = []
            print('Insira as informacoes do livro')
            cod = int(input('digite o codigo do livro: '))
            if cod == 0:
                a = int(input('digite 1 para parar e 2 para continar'))
                if a == 1:
                    break
            ti = input('digite o titulo: ')
            if ti == 0:
                a = int(input('digite 1 para parar e 2 para continar'))
                if a == 1:
                    break
            nautor = int(input('digite o numero de autores: '))

            for autor in range(nautor):
                autor = input(f'Digite o nome do {autor} autor:')
                lista_autores.append(autor)
            if nautor == 0:
                a = int(input('digite 1 para parar e 2 para continar'))
                if a == 1:
                    break
            pre = float(input('digite o preço do livro: '))
            if pre == 0:
                a = int(input('digite 1 para parar e 2 para continar'))
                if a == 1:
                    break
            lista.append(cod)
            lista.append(ti)
            lista.append(nautor)
            lista.append([lista_autores])
            lista.append(pre)

        #correcao de informacoes
        #validacoes variaveis