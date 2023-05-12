#Desenvolva um programa que leia o primeiro termo e a razão de uma pa.
# no final mostre os 10 primeiros termos dessa progressao 

#primeiro_termo = int(input("Insira o primeiro termo da PA: "))
#razao_pa = int(input("Digite a razao da PA: "))

#decimo_termo= primeiro_termo +(10-1)*razao_pa

#for c in range(primeiro_termo,decimo_termo+razao_pa,razao_pa):

#    print(f"{c}", end=" -> ")



primeiro_termo = int(input("Insira o primeiro termo da PA: "))
razao_pa = int(input("Digite a razao da PA: "))
decimo_termo= primeiro_termo+(10*razao_pa)
for c in range(primeiro_termo,decimo_termo,razao_pa):
    print(c, end=" -> ")