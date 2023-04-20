# Função para calcular o fatorial de um número
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Loop para ler vários números inteiros e calcular o fatorial
while True:
    n = int(input("Digite um número inteiro positivo (ou um número negativo para sair): "))
    if n < 0:
        break
    print("{}! = {}".format(n, fatorial(n)))
