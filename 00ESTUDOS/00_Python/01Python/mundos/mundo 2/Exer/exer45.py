# crie um programa que faça o computador jogar jokenpo com voce 

##from time import sleep
##from random import randint

##print('Escolha uma opção para jogar contra o computador!')
##b= randint(1,3)
##print('''   1- Tesoura  
  # 2- Pedra    
   #3- Papel:''')
#a = (int(input('Qual sua escolha:')))
#print('Carregando...')
#sleep(2)
#print("Jokn")

#if a == b:
    #print('Deu empate! Nos dois jogamos {}.'.format(b))
#elif a == 1 and b == 2:
   # print('Tesoura perde para Pedra! O computador ganhou jogando {} contra seu {}.'.format(b,a))
#elif a == 1 and b == 3:
   # print( 'Tesoura ganha do Papel! Parabens voce ganhou!')
#elif a == 2 and b == 3:
  #  print('Pedra perde para o Papel! O computador ganhou jogando {} contra seu {}.'.format(b,a))
#elif a == 2 and b == 1:
  #  print('Pedra ganha de tesoura! Parabens voce ganhou!')
#elif a == 3 and b == 1:
   # print('Papel perde para tesoura! O computador ganhou jogando {} contra seu {}.'.format(b,a))
#elif a == 3 and b == 2:
 #   print('Papel ganha de Pedra! Parabens voce ganhou!')
#else:
 #   print('Digite um valor valido de 1 a 3')

from random import randint 
from time import sleep
itens = ('Pedra','Papel','Tesoura') # para computador e jogador escolherem em lista
computador = randint(0,2)
#print("O computador escolheu {}.".format(itens[computador]))  #Vou pegar um item de acordo com o que o computador mandar
print('''  0- Pedra  
  1- Papel    
  2- Tesoura''')
jogador = (int(input('Qual sua escolha:')))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-='*15)
print('Computador jogou {}'.format(itens[computador])) ##na posição itens pegue o numero correspondente ao computador
print('Jogador jogou {}'.format(itens[jogador]))##na posição itens pegue o numero correspondente a jogador
print('-='*15)

if computador == 0: #jogou pedra
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("Jogador Vence!")
    elif jogador == 2:
        print("Computador Vence!")
    else:
        print('Jogada invalida!')

elif computador == 1: #jogou papel
    if jogador == 0:
        print('Computador Vence!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador Vence!')
    else:
        print('Jogada invalida!')

elif computador == 2: #jogou tesoura
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('Jogador Perde!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada invalida!')
