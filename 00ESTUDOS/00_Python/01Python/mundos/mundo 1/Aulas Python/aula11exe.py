cores = {'limpa':'\033[m',
'azul':'\033[34m',
'amarelo':'\033[33m',
'pretoebranco':'\033[7;30m',
'azuleamelo':'\033[1;37:44m',}


# 0 sem estilo 1 negrito 4 sublinhado 7 negativo
# 30 branco 31 vermelho 32 verde 33 amarelo 34 azul 35 roxo 36 azul claro 37 cinza
# 40 até 47 as mesmas cores para back


print('Letras0Sem estilo''  \033[0mAAAAAAAAAAAAA\033[m')
print('Letras1 negrito''  \033[1mAAAAAAAAAAAAA\033[m')
print('Letras2normal''  \033[2mAAAAAAAAAAAAA\033[m')
print('Letras3inclinado''  \033[3mAAAAAAAAAAAAAA\033[m')
print('Letras4sublinhado''  \033[4mAAAAAAAAAAAAA\033[m')
print('Letras5normal''  \033[5mAAAAAAAAAAAAA\033[m')
print('Letras6normal''  \033[6mAAAAAAAAAAAAA\033[m')
print('Letras7 invertido' '\033[7mAAAAAAAAAAAAA\033[m')
print('-=-'*20)

print('CORES1 -''\033[;1mAAAAAAAAAAAA\033[m')
print('CORES2 -''\033[;2mAAAAAAAAAAAA\033[m')
print('CORES30 -''\033[;30mAAAAAAAAAAAA\033[m')
print('CORES31 -''\033[;31mAAAAAAAAAAAA\033[m')
print('CORES32 -''\033[;32mAAAAAAAAAAAA\033[m')
print('CORES33 -''\033[;33mAAAAAAAAAAAA\033[m')
print('CORES34 -''\033[;34mAAAAAAAAAAAA\033[m')
print('CORES35 -''\033[;35mAAAAAAAAAAAA\033[m')
print('CORES36 -''\033[;36mAAAAAAAAAAAA\033[m')
print('CORES37 -''\033[;37mAAAAAAAAAAAA\033[m')
print('-=-'*20)
print('Plano de fundo 40 -''\033[;;40mAAAAAAAAAA\033[m')
print('Plano de fundo 41 -''\033[;;41mAAAAAAAAAA\033[m')
print('Plano de fundo 42 -''\033[;;42mAAAAAAAAAA\033[m')
print('Plano de fundo 43 -''\033[;;43mAAAAAAAAAA\033[m')
print('Plano de fundo 44 -''\033[;;44mAAAAAAAAAA\033[m')
print('Plano de fundo 45 -''\033[;;45mAAAAAAAAAA\033[m')
print('Plano de fundo 46 -''\033[;;46mAAAAAAAAAA\033[m')
print('Plano de fundo 47 -''\033[;;47mAAAAAAAAAA\033[m')
print('-=-'*20)
print('MIX0;1;42 ''\033[;1;42mAAAAAAAAAAAAAAAAAAAA\033[m')
print('MIX0;1;45 ''\033[;1;45mAAAAAAAAAAAAAAAAAAAA\033[m')
print('MIX0;1;46 ''\033[;1;46mAAAAAAAAAAAAAAAAAAAA\033[m')
print('MIX0;32;46 ''\033[1;36;46mAAAAAAAAAAAAAAAAAAAA\033[m')
print('MIX0;1;47 ''\033[;1;47mAAAAAAAAAAAAAAAAAAAA\033[m')