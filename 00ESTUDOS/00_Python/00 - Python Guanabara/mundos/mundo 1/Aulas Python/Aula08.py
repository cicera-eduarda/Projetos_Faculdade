#Utilização de biblioteca

#Funcionalidades modulos biblioteca função
#incluir algo import
#from doce import pudim dando ordem especifica do item
#import bebida todas as bebidas
#math biblioteca
#ceil arredondamento para cima  ## funçoes
#floor para baixa
#trunc
#pow potencia
#sqrt raiz quadrada
#factorial 
##import math importa tudo gasta memoria 
## frrom math import sqrt,ceil importa so o que vou usar importação otimizada 
## para visualizar quais bibliotecas utilizar olhar biblioteca  no python varias criadas
##posso importar essas bibliotecas 
##posso criar minha propria modulo/biblioteca e disponibilar na comunidade


# from doce import pudim - importar so o pudim
#import doce - importa todos os doce

# biblioteca de matematica math 
#math ceil floor trunc pow sqrt factorial

from math import sqrt, ceil ##importação das funções que eu preciso da biblioteca de matematica importe sqrt

a = int(input('Digite um numero:'))
raiz = sqrt(a) ##QUando importo da biblioteca o item não é necessario adicionar math. antes do item
print('A raiz do numero é {:.2f}'.format(raiz))

import math  ## importação da biblioteca (modulo) toda

num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print('A raiz de um numero {} é igual a raiz sem arredondamento {:.2f}.'.format(num, (raiz)))
print('A raiz de um numero {} é igual a raiz com arredondamento positivo {:.2f}.'.format(num, math.ceil(raiz))) ##arredondar raiz para cima
print('A raiz de um numero {} é igual a raiz com arredondamento negativo {:.2f}.'.format(num, math.floor(raiz))) ## arredondar para baixo

import random # o computador gera um numero aleatorio
b = random.random()  # gera um numero aleatorio entre 0 e 1 
print('{:.2f}'.format(b))

c = random.randint(1,100) #um numero aleatorio 
print('{:}'.format(c))

import emoji ##importar bibliotecas diretamente da rede pip install 
print(emoji.emojize("Ola Mundo :sunglasses::earth_americas:", use_aliases=True))




