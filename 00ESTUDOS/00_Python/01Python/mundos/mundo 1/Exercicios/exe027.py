#Faça um programa que leia o nome completo de uma pessoa e mostrando em seguida o primeiro e o ultimo nome separadamente
#ex ana maria 
#primeiro ana
#ultimo souza
nome = str(input('Qual seu nome:')).strip()
nome.split()
print(f'O primeiro nome é {nome.split()[0]}')
print(f'O segundo nome é {nome.split()[-1]}')
##nome.n = nome.split()
##print('Seu ultimo nome é {}'.format(nome.n[len(nome)-1]))
