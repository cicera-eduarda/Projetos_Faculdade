##Condições
# - Em uma condição ou o bloco verdadeiro e executado ou o bloco falso é executado
# if estrututra simples
# if else para estrutura composta 

##se carro.esquerda ()
##  bloco_v_

## if carro.esquerda():
## bloco True

## se carro.direita(): 
#   bloco_F_

## if carro.direita():
#   bloco False

tempo = int(input('Quantos anos tem seu carro?'))

if tempo <=3:   #COMANDO ALINHADO EXECUTADO SEMPRE
    print('Carro novo') #COMANDO NAO ALINHA TALVEZ SEJA OU NAO
else:
    print('Carro velho')
print('---FIM ---')

##CONDIÇÃO SIMPLIFICADA

TEMPO =int(input('Quantos anos tem o seu carro?'))
print('carro novo' if tempo <=3 else 'carro velho')
print('---Fim---')

### desafio


nome = str(input('Qual seu nome? ')).strip().capitalize()
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else: 
    print('Você tem um belo nome!')
print('Bom dia {}'.format(nome))

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda note:'))
media = (n1+n2)/2
print('A sua media final foi {:.1f}'.format(media))
print('Parabens sua media foi boa' if media>=6 else 'ESTUDE MAIS')


if media >= 6.0:
    print('Sua media foi boa')
else:
    print('Sua media foi insuficiente')



###Desafios 

##Escreve um programa que faça o computador ''pensar'' em um numero inteiro entre 0 e 5 e peça para o usuarui tentar descobrrir qual foi 
## o numero escolhido pelo computador
## o programa devera escrever na tela se o usuario acertou ou perdeu
## utilizar modulo de sorteio de numero aleatorio comparar o resultado obtido com o digitado pelo usuario 
#random.randint()  # gera um numero aleatorio entre 0 e 1 


