#Escreva um programa que leia um numero inteiro  qualquer e peça para o usuario escolher qual serra a base de conversão:
# 1 para binario 2 para octal 3 hexadecimal

n = int(input('Insira um numero inteiro:'))
print(('Escolha a base para conversão:' ))
print('''(1) binario
(2) octal
(3) hexadecimal''')
a = int(input('Digite sua escolha:'))

if a ==1:
    print('{} convertido para BINARIO é igual a {}.'.format(n,bin(n)[2:])) ##opção de fatiamento apartir de 2
elif a == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(n,oct(n)[2:]))
elif a == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção invalida!Escolha uma opção de 1 a 3')


#0b para binario e assim por diante 