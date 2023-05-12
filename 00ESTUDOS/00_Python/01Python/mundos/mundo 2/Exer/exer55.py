#Faça um programa que leia o peso de cinnco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos

maior_peso=0
menor_peso=0

#primeira ocorrencia - sera maior e menor
for p in range(1,6):
    peso=float(input(f"Digite o peso da {p}º pessoa: "))
    #peso da primeira pesoa
    if p ==1:
        maior_peso=peso
        menor_peso=peso
    else:
     if peso>maior_peso:
        maior_peso=peso
     if peso<menor_peso:
        menor_peso=peso

print(f"O menor peso digitado foi de {menor_peso} e o maior peso foi de {maior_peso}")
