##Exercicio 19 ##

from random import choice 

a = str(input('Digite o primeiro aluno:'))
b = str(input('Digite o segundo aluno:'))
c = str(input('Digite o terceiro aluno:'))
d = str(input('Digite o quarto aluno:'))
lista =[a,b,c,d]
escolhido = choice(lista)
print('O ALUNO escolhido foi ''\033[1;34m''{}''\033[m''.'.format(escolhido))