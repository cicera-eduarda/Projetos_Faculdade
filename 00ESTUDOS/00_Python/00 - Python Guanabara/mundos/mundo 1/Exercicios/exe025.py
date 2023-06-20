#Crie um programa  que leia o nome de uma pessoa e diga se ela tem silva no nome 
NOME=(str(input('Digite um nome:'))).strip()
print('Seu nome tem Silva?{}'.format('SILVA' in NOME.upper()))