### Condições aninhadas 
##nao se baseia somente em verdadeiro ou falso 

nome = str(input('\033[34;32mQUAL SEU NOME?\033[m'))

if nome == 'Gustavo': ## simples
    print('Que nome bonito!')

print('Tenha um bom dia, {}!'.format(nome))

print('*-*'*20)

if nome == 'Gustavo': ## condição composta
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))

print('*-*'*20)

if nome == 'Gustavo': ## condição aninhada
    print('Que nome bonito!')
elif nome in 'Ana Claudia Paula':
    print('Voce tem um pelo nome feminino!')
elif nome == 'Pedro' or 'Maria': ## nao funciona
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))

print('*-*'*20)


 ## condição aninhada
if nome == 'Gustavo':
    print('É um belo nome!') 
elif nome == 'Ana' or nome== 'Maria' or nome=='Paulo':
        print('É um belo nome feminino!')
else:
    print('Você de novo?')
print('Tenha um bom dia!')

