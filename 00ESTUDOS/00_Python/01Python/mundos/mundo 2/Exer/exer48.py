#Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos 
#de tres e que se encontram no intervalo de 1 ate 500

soma=0
contador=0
for c in range(1,501):
    if c%3==0 and c%2!=0: #multiplo de 3 e impar == 12 é par
        soma+=c
        contador+=1

print(f"A soma de todos os {contador} valores é {soma}")
