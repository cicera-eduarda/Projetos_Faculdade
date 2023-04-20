
soma = 0
impares=0

a = int(input("Insira a quantidade de numeros desejada: "))

for i in range (a):
    b = int(input("Digite o numero desejado "))

    if b %2==0:
        soma+=b
        
    else:
        impares+=1

print(f"Resultado soma {soma} Resultado impares {impares}")