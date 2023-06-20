#Faça um programa que e leia o ano de nascimento de um jovem e informe, de acordo com sua idade 
# se ele ainda vai se alistar ao serviço militar
#se a hora de se alistar
# se ja passou do tempo do alistamento 
# seu programa tambem devera mostrar o tempo que falta ou que passou do prazo

from datetime import date


print('\033[1;31mCadastro Exercito\033[m')

nome = str(input('Qual seu nome? '))
ano = int(input('Insira seu ano de nascimento:'))
hoje = date.today().year
idade = ((hoje)- ano)

if idade == 18:
    print('{} este é o ano de seu alistamento pois voce esta com {} anos'.format(nome,idade))
elif idade > 18:
    anoalistamento = ano + 18
    print('{} o seu tempo de alistamento já passou em {} anos, deveria ter ocorrido em {} , procure um posto de alistamento!'.format(nome,(idade-18),anoalistamento))
    
else: 
    print( '{} seu alistamento deve ocorrer em {} anos. Não perca a data!'.format(nome,(18-idade)))

##adicionar sexo na identificação