#Validação de informações 

#faça um programa que leia o sexo de uma pessoa, mas so aceite os valores M 
#ou F. Caso esteja errado, peça a digitação novamente ate ter um valor correto.


sexo=str(input(f"Digite o sexo [F/M]: ")).strip().upper()[0] #tirar os espaço do inicio e final, jogar para maiusculo, pegar somente a primeira letra


while sexo not in 'MmFf': #CASO O DADO ESTEJA INVALIDO CAI AQUI, CASO ESTEJA CERTO O PROGRAMA SEGUE EM FRENTE
    sexo=str(input("Dados invalidos. Digite novamente: ")).strip().upper()[0]

print(f"Sexo {sexo} registrado com sucesso!")