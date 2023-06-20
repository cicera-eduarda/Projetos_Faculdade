#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda nao atingiram a maioridade 
#e quantas ja sao maiores

import datetime
data=datetime.datetime.now()
soma=0
soma1=0

for i in range(1,8):
    ano_nascimento=int(input(f"Digite ano de nascimento {i} EX: 1997: "))
    
    if data.year-ano_nascimento>=18:
        soma+=1
        
    else:
        soma1+=1

print(f"Pessoas maiores de idade {soma}, pessoas menores de idade {soma1}")