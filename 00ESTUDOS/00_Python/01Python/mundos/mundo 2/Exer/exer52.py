#Faça um programa que leia um numero inteiro e diga se ele e ou nao um numero primo
#por 1 e por ele mesmo

total = 0

num=int(input("Digite um numero: "))

for c in range(1,num+1):
    if num%c==0 and num%num==0:
       print(f'\033[33m', end=" ")
       print(f'{c}', end=' ')
       total+=1
    else:
        print('\033[31m',end = ' ')
        print(f'{c}', end='')

print(f"\033[mO numero {num} foi dividido {total} vezes")
