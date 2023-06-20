#Crie um programa que leia um numero inteiro e mostre na tela se é par ou impar
numero = int(input('Digite um numero inteiro:'))

if numero%2 ==0:
    print(f'O numero {numero} é par!')
else:
    print(f'O numero {numero} é impar')