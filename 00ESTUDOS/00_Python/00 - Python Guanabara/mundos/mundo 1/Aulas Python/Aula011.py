##Cores no Terminal

#ANSI (espacape sequence)



#\033[style;text;back m
# 0 sem estilo 1 negrito 4 sublinhado 7 negativo
# 30 branco 31 vermelho 32 verde 33 amarelo 34 azul 35 roxo 36 azul claro 37 cinza
# 40 até 47 as mesmas cores para back


print('\033[1;30;41mteste01') #vermelho e preto

print('\033[4;33;44mteste02') # azul e amarelo

print('\033[1;35;43mteste03') # amarelo e roxo

print('\033[30;42mteste04') # verde e roxo

print('\033[mteste05') ## volta ao normal

print('\033[7;30mteste06') #preto e cinza


a = 5
b = 6

print('\033[mAs variaveis são \033[0;30m{}\033[m e \033[0;33m{}\033[m sendo respectivamente a e b'.format(a,b))

print('Ola mundo')

s = 'prova de python'
print(len(s))

x = 'curso de python no cursoemvideo'
print(x[:5]) #PEGA AS PRIMEIRAS CINCO LETRAS NÃO DO O COMEÇO SÓ O FINAL
print(x[5:])
print(x[0])

 #bool / True / False 


nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}.'.format('\033[4;34m',nome,'\033[m'))


nome = 'Moacyr'
cores = {'limpa':'\033[m',
'azul':'\033[34m',
'amarelo':'\033[33m',
'pretoebranco':'\033[7;30m',
'azuleamelo':'\033[1;37:44m',}
# 0 sem estilo 1 negrito 4 sublinhado 7 negativo
# 30 branco 31 vermelho 32 verde 33 amarelo 34 azul 35 roxo 36 azul claro 37 cinza
# 40 até 47 as mesmas cores para back

print('Olá! Muito prazer em te conhecer, {}{}{}.'.format(cores['pretoebranco'],nome,cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}.'.format(cores['azul'],nome,cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}.'.format(cores['amarelo'],nome,cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}.'.format(cores['azuleamelo'],nome,cores['limpa']))