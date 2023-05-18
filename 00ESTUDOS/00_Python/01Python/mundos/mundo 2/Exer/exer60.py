#Faça um programa que leia um numero qualquer e mostre o seu fatorial
#ex 5! = 5*4*3*2*1 = 120


#from math import factorial
#n=int(input("Digite um numero: "))
#fatorial= factorial(n)
#print(f"O fatorial de {n} é {fatorial}")


n = int(input("Insira um numero: "))
c = n 
f = 1

while c>0:
    print(f'{c}', end=' ')
    print(f"x " if c>1 else '=', end='')  #sintaze interessante
    c-=1
