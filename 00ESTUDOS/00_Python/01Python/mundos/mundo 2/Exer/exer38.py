#escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
#o primeiro valor é maior 
#o segundo valor é maior
#nao existe valor maior os dois são iguais

print('Comparando dois numeros')

n1= int(input('DIGITE UM NUMERO:'))
n2= int(input('DIGITE O SEGUNDO NUMERO:'))

if n1>n2:
    print('O primeiro valor é o maior')
elif n1<n2:
    print('O segundo valor é o maior')
else:
    print('Ambos os numeros são iguais')
    