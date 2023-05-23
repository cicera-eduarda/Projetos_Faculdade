#Melhore o desafio 61, perguntando para o usuario se ele quer mostar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

print(f'{"Gerador de PA":^20}')
print('-'*20)
primeiro=int(input("Insira o primeiro termo:"))
razao=int(input("Insira a razao: "))
termo=primeiro
c = 1

while c <=10: #enquanto c menor ou igual a 10 faz o loop
    #demais termos
    print(f"O termo numero {c} e igual a {termo}")
    termo +=razao
    c+=1


