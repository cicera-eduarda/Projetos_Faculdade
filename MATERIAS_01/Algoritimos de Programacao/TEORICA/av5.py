#Construir um programa que faz a leitura de N dados de cadastro de games contendo: nome do jogo (string), empresa (string), ano de
#lançamento (int) e tipo(string). Os dados dos games devem ser, obrigatoriamente, armazenados numa estrutura de lista, com sublistas,
#como no exemplo dado em classe. 
#Após o trecho da leitura dos dados dos N games e a montagem da lista, fazer a leitura de uma
#determinada empresa e de um período: ano_inicio e ano_final e, o programa, deve imprimir os dados (TODOS OS CAMPOS) dos games que
#atendam os valores lidos: empresa e ano de lançamento dentro do período. Além disso, no final, deverá imprimir o total de games nestas
#condições. Verificar se a lista está vazia e, se estiver vazia, imprimir mensagem. O valor de N deve ser lido e maior do que zero - valide.
#Repita a leitura de N até que seja lido um valor maior ou igual a zero. Não utilizar método ou função pronta de lista para a solução do
#problema, com exceção de append e len, se necessário. Seu programa deve demonstrar seu conhecimento de percorrer elementos de uma
#lista.


jogos =[]
total_jogos = 0

#limite laco e validacao

while True:
    N = int(input("Numero de total de jogos para serem cadastrados: "))
    if N>0: 
        break

#entrada valores

for jogo in range(N):

    nome= input("Digite o nome: ").upper()
    empresa = input("Digite a empresa: ").upper()
    ano = int(input("Ano: "))
    preco = float(input("Preco: R$"))

    #adicao a lista
    jogos.append([nome, empresa, ano, preco])

#Entrada busca

empresa_busca = input("Insira a empresa para busca: ").upper()
ano_inicio = int(input("Insira o ano inicial para busca: "))
ano_final = int(input("Insira o ano final para busca: "))

#Percorrer a lista para busca

print(f"Jogos da empresa {empresa_busca} no periodo de {ano_inicio} e {ano_final}")

for jogo in jogos:

    # procurar no indice 1 (empresa) se é igual ao valor buscado em empresa_busca e ano>jogo(ano)>ano
    #lista se inicia em 0

    if jogo[1] == empresa_busca and ano_final>= jogo[2]<=ano_final:

        print(f"\n\nNome: {jogo[0]} Empresa: {jogo[1]} Ano: {jogo[2]} Preco: {jogo[3]:.2f}")
        total_jogos+=1

if total_jogos>0:

    print("Total de Jogos:",total_jogos)
else:
    print("Não ha jogos na condição de busca")
