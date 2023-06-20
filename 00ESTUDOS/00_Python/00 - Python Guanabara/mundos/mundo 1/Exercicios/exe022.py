## Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiuscula
#o nome com todas as letras minuscola
# Quantas letras ao todo sem considerar os espaços
#Quantas letras tem o primeiro nome

nome =(str(input('Digite seu nome completo:'))).strip() ##strip retira espaços desnecessarios
print('O nome em maiusculo:',nome.upper().strip())
print('O nome com todas as letras minusculas:', nome.lower().strip())
#### Eliminando os espaços dentro da frase 
print('O nome completo tem {} letras'.format(len(nome.replace(" ",""))))##substitui os espaços por junto
print('O nome completo tem {} letras'.format(len(nome)-nome.count(' '))) ##contei os espaços


print('O nome completo com os espaços tem {} letras.'.format(len(nome)))
partes=nome.split() #separa em partes em listas
print('O primeiro nome é',(partes[0]))
print('O primeiro nome tem {} letras.'.format(len(partes[0])))
### OUTRA MANEIRA DE ACHAR O NUMERO DE LETRAS DO PRIMEIRO NOME
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) ##Encontrando o primeiro espaço depois do nome
