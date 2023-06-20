#Crie um programa que mostre na tela todos os numeros pares que estao no intervalo de 1 a 50.

contador=0
for c in range(2,51,2):
    if c%2==0:
        contador+=1
        print(f"{c}", end=',')

print(f"Existem {contador} numeros pares neste intervalo")