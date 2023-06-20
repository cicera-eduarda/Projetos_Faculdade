#refaça o exercicio desafio 009 mostrando a tabuada de um numero 
#que o usuario escolher so que agora utilizando um laço for

print(f"{'Tabuada':^20}")

numero= float(input("Insira um numero qualquer para obter sua tabuada:"))

for n in range(0,11):
    print(f"{numero}x{n} = {numero*n:.1f}")