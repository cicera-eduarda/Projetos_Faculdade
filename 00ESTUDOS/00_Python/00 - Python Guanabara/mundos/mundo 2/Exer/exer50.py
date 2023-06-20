#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas 
#daqueles que foram pares. Se o valor digitado for impar desconsidere-o

soma=0
contador=0

for n in range(1,7):
    num=int(input(f"Digite o {n}º numero inteiro: "))
    if num%2==0:
        soma+=num
        contador+=1

print(f"A soma dos numeros digitados {contador} é {soma}")
    
