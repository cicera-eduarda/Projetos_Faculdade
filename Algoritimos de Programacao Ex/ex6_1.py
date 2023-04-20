

entrevistados= int(input("Insira o numero de entrevistados "))
salario_total=0
filhos_total=0
qtd_pessoas_100=0
salario=0
filhos=0
qtd_pessoas= 0

percentual_pessoas=0
maior_salario=0

while entrevistados >0:
    entrevistados-=1
    qtd_pessoas+=1
    print(f"Entrevistado numero {qtd_pessoas}")
    salario=(float(input("Insira o salario: ")))
    filhos = (int(input("Insira o numero de filhos: ")))

    salario_total +=salario
    filhos_total +=filhos

    if maior_salario<salario:
        maior_salario= salario

    if salario<=100:
        qtd_pessoas_100+=1

media_salario = salario_total/qtd_pessoas
media_filhos = filhos_total/qtd_pessoas
percentual_pessoas = (qtd_pessoas_100*100)/qtd_pessoas

print(f"\n\nMedia do salario da população  {media_salario}")
print(f"Media do numero de filhos {media_filhos}")
print(f"Maior salario {maior_salario}")
print(f"Percentual de pessoas com salario ate 100 reais é de {percentual_pessoas}")
