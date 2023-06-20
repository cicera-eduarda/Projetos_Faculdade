##Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
cores ={'limpa':'\033[m',
'azul':'\033[;32m',
'verde':'\033[;34m'}

n = int(input('\033[;32m''Digite um numero:''\033[m'))
a = int(n + 1)
b = int(n - 1)
print('O numero ''\033[;32m''{}''\033[m'' possui como antecessor ''\033[;32m''{}''\033[m'' e sucessor''\033[;32m'' {}''\033[m'.format(n,b,a))
print('O numero {} possui como sucessor {} e antecessor {}'.format(n, (n+1),(n-1)))

## Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um numero:'))
a = (n*2)
b = (n*3)
c = (n ** (1/2))
print('O numero {}, possui como dobro {}, triplo {} e tem como raiz quadrada {:.3f}'.format(n,a,b,c))
print('O numero {}, possui como dobro {}, triplo {} e tem como raiz quadrada {:.3f}'.format(n,(n * 2),(n * 3),(n ** (1/2))))
print(pow(n,(1/2)))

## Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

a = float(input('Insira a primeira nota: '))
b = float(input('Insira a segunda nota: '))
c = float((a+b)/2)
print('A media do aluno é {:.3f}.'.format(c))

##EScreva um programa que leia um valor em metros e exiba convertido em centrimetros e milimetros
n = float(input('Digite um valor em metros: '))
a = n * 100
b = n * 1000
print('O valor {:.0f}, em centimetros {:.0f}, o valor em milimetros {:.0f}.'.format(n,a,b))

##Calculadora, faça um programa que leia um numero inteiro e retorne a tabuada 
n = int(input('Digite um numero para ver sua tabuada:'))
a = n * 1
b = n * 2
c = n * 3
d = n * 4
e = n * 5
f = n * 6
g = n * 7
h = n * 8 
i = n * 9
j = n * 10
print('{} x {} = {}'.format(n, 1, a))
print('{} x {} = {}'.format(n, 2, b))
print('{} x {} = {}'.format(n, 3, c))
print('{} x {} = {}'.format(n, 4, d))
print('{} x {} = {}'.format(n, 5, e))
print('{} x {} = {}'.format(n, 6, f))
print('{} x {} = {}'.format(n, 7, g))
print('{} x {} = {}'.format(n, 8, h))
print('{} x {} = {}'.format(n, 9, i))
print('{} x {} = {}'.format(n, 10,j))

n = int(input('Digite um numero para ver sua tabuada:'))
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {:2} = {}'.format(n, 10, n * 10))

##Conversor de moeda
##Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar
#considere US$ 1,00 = R$ 3,27

N = float(input( 'Quanto dinheiro você tem?R$'))
d = float(N/3.247)
print('Você pode comprar com {}, US${:.3f}.'.format(N,N/3.247))
print('Voce pode comprar com esse valor {:.2f} dolares'.format(d))
