#DESENVOLVA UM PROGRAMA QUE LEIA O NOME IDADE E SEXO DE 4 PESSOAS. 
#NO FINAL O PROGRAMA MOSTRA: a MEDIA DE IDADE DO GRUPO. qual o nome do 
#homem mais velho, quantas mulheres tem menos de 20 anos

idades=0
idade_homem=0
homem_velho=''
mulheres_20= 0

for p in range(1,5):
    pessoa=input("Insira o nome: ").upper()
    sexo=input("Insira o sexo [F/M]: ").upper()
    idade= int(input("Insira a idade: "))
    idades+=idade

    if sexo=='F' and idade<20:
        mulheres_20+=1
    elif sexo=='M' and idade>idade_homem:
        homem_velho=pessoa
    
media=idades/4

print(f"Media de idade do grupo: {media}. Homem mais velho {homem_velho}, quantidade de mulheres com menos de 20 anos {mulheres_20} ")





        