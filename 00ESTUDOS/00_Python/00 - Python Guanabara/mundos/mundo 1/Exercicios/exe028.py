###Desafios 

##Escreve um programa que faça o computador ''pensar'' em um numero inteiro entre 0 e 5 e peça para o usuarui tentar descobrrir qual foi 
## o numero escolhido pelo computador
## o programa devera escrever na tela se o usuario acertou ou perdeu
## utilizar modulo de sorteio de numero aleatorio comparar o resultado obtido com o digitado pelo usuario 
#random.randint()  # gera um numero aleatorio entre 0 e 1 
from time import sleep
numero = int(input('Digite um numero de 0 a 5:'))
print('-=-'*25)
from random import randint
sorte = randint(0,5)
print('PROCESSANDO...')
sleep(2)    ## faz o computador demorar um pouco para responder
if numero == sorte:
    print('Voce acertou! O numero escolhido foi o mesmo que o sorteado!')
else:
    print('Voce errou! O seu numero escolhido foi {}, mas o numero sorteado foi {}'.format(numero, sorte))
print('tente novamente')