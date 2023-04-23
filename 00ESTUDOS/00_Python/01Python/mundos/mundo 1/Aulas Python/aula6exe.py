# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.
# ele pode ser um numero, alfabetico tem caracter maiusculo, minusculo

cores={'limpa':'\033[m',
'cor1':'\033[;32m',
'cor2':'\033[;34m'}

n = input('Digite um valor: ')

print('Este valor' ,n, ' consta como',n.isalnum(), 'para números') # é um numero?
print('Este valor' ,n, 'consta como',n.isalpha(), 'para letras')# é uma letra
print('Este valor' ,n, 'consta como',n.isalnum(), 'para combinação alphanumerica') # é uma combinação alpha numerica
print('Este valor' ,n, 'consta como',n.isupper(), 'para letras maiuscula') # tem somente letras maiusculas
print('Este valor' ,n, 'consta como',n.islower(), 'para letras minuscula') # tem somente letras minusculas


a = input('Digite algo...') ##input retorna sempre uma string
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços?', a.isspace())  ##somente espaços
print('É um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Esta em letras maiuscula?', a.isupper())
print('Esta em letras minusculas?', a.islower())
print('Esta capitalizada?', a.istitle()) ##nem maiuscula nem minuscula esta capitalizada 

B = input('Digite algo...')
print('O tipo primitivo de {}{}{} é'.format(cores['cor1'],B,cores['limpa']) ,type(B))
print('O valor de {}{}{}.Só tem espaços?'.format(cores['cor1'],B,cores['limpa'], B.isspace()))  ##somente espaços
print('O valor de {}{}{}.É um numero?'.format(cores['cor1'],B,cores['limpa']), B.isnumeric())
print('O valor de {}{}{}.É alfabetico?'.format(cores['cor1'],B,cores['limpa']), B.isalpha())
print('O valor de {}{}{}.É alfanumérico?'.format(cores['cor1'],B,cores['limpa']), B.isalnum())
print('O valor de {}{}{}.Esta em letras maiuscula?'.format(cores['cor1'],B,cores['limpa']), B.isupper())
print('O valor de {}{}{}.Esta em letras minusculas?'.format(cores['cor1'],B,cores['limpa']), B.islower())
print('O valor de {}{}{}.Esta capitalizada?'.format(cores['cor1'],B,cores['limpa']), B.istitle())