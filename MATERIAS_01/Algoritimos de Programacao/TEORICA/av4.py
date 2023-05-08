#Escreva um programa que imprima na tela os dez primeiros múltiplos de um
#número inteiro qualquer fornecido pelo usuário. No final, imprima também a soma
#destes dez números.

multiplicacao=1
soma=0
num = 10
multiplos= []

n = int(input("Digite um numero inteiro para ter seus 10 primeiros multiplos e sua soma: "))

for i in range (1,11):

    multiplicacao= i*n
    soma+=multiplicacao
    multiplos.append(multiplicacao)

print(f"Valor de Entrada:{n} ")
print(f"Lista de Multiplos: {multiplos}")
print(f"Soma: {soma}")
