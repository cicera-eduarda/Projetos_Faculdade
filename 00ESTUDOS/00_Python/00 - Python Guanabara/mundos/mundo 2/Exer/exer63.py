#Escreve um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci
#ex: 0-1-1-2-3-5-8

n = int(input("Insira um numero inteiro: "))
c=1
TERMO1= 0
TERMO2= 1
PROXIMO_TERMO = 0

while c<n:
    PROXIMO_TERMO=TERMO1+TERMO2
    c+=1
