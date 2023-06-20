#16 #Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira. Exe 6,127 retorna 6

#17 #faça um progrma que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo calcule e mostre o comprimento da
#hipotenusa 

#18 #faça um program que leia um angulo qualquer e mostre na tela o valor do  seno, cosseno e tangente desse angulo

#19 # um professor quer sortear um dos seus quatro alunos para apagar o quadro . Faça um programa que ajude ele, lendo o nome deles e
#  escrevendo  o nome escolhido

#20 # um professor quer sortear a ordem de apresentação  de trabalhos dos alunos. Faça um programa qe leia o nome dos quatro alunos
# e mostre a ordem  sorteada

#21 # Faça um programa em python que abra e reproduza o audio de um arquivo mp3 


## Exercicio 16 ###
a = float(input('Digite um numero:'))
print(int(a))
print('{:.0f}'.format(a)) ## desta maneira arredonda


## Exercicio 17 ##

b = float(input('Insira o valor do cateto oposto em cm do triangulo:'))
c = float(input('Insira o valor do cateto adjacente em cm do triangulo:'))
import math
d = math.hypot(math.sqrt(b*b + c*c))
hipo = math.hypot(b,c)
print('O valor dos quadrados dos catetos para {:.2f} e {:.2f} são respectivamente {:.2f} e {:.2f}, tendo como resultado o valor {:.2f} para hipotenusa.'.format(b, c, (b*b), (c*c), d))
print('O valor da hipotenusa é {:.2f}'.format(hipo))


## Exercicio 18 ##
e = float(input('Digite o angulo em graus:'))
 ##só aceita radianos
from math import radians, sin, cos, tan ## posso importar somente os elementos que eu vou usar
rad = radians(e)
f = cos(rad)
g = sin(rad)
h = tan(rad)
print('O valor do angulo {} em radianos é {:.3f}, sendo seu cosseno, seu seno respectivamente e sua tangente  {:.3f}, {:.3f} e {:.3f}'.format(e, rad, f, g, h))

e = float(input('Digite o angulo em graus:'))
import math
f = math.cos(math.radians(e)) ##outra maneira
g = math.sin(math.radians(e))
h = math.tan(math.radians(e))



##Exercicio 19 ##

from random import choice 

a = str(input('Digite o primeiro aluno:'))
b = str(input('Digite o segundo aluno:'))
c = str(input('Digite o terceiro aluno:'))
d = str(input('Digite o quarto aluno:'))
lista =[a,b,c,d]
escolhido = choice(lista)
print('O ALUNO escolhido foi {}.'.format(escolhido))