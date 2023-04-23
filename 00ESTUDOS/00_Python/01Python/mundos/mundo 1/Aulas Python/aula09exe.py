cores={
    'limpa':'\033[m',
    'azul':'\033[;32m',
    'verde':'\033[:34m' }

frase = '     Curso em Video Python             '
print('\033[1;34m',frase,'\033[m')
print(frase[13])
print(frase[1:15:2])
print(frase[::2]) #salto em duas em duas letras
print('Oi')
print("""{}Welcome! Are you completely new programming?
About why and how to get started with Python. Fortunately
an experienced programmer in any programming language.
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!{}""".format(cores['azul'],cores['limpa'])) ## Tres aspas

print(frase.count('o')) ##tres vezes o maiscula
print(frase.upper().count('o')) ## coloquei tudo em maiscula para contar
print(len(frase))
print(len(frase.strip())) ## remove todos os espaços adicionais do final ou começo
print(frase.replace('Python', 'Android')) ##substituir itens
frase = frase.replace ('Python', 'Android') ##string é imutavel a menos que eu utilize uma ferramenta para tal
print('Curso' in frase) # existe na frase essa palavra
print(frase.find('Video')) #onde esta video
print(frase.find('video')) #onde esta video ##não existe -1
print(frase.lower().find('video'))## dentro da frase jogando tudo para minusula existe a palavra video minuscula
frase = frase.replace('Android','Python')
print(frase.split()) ## cria uma lista com a frase
dividido = frase.split()
print(dividido[0])#dividido é uma lista, portanto posso mostrar o primeiro item desta lista
print(dividido[2][3]) #pega o dividido 2 que é video e me mostre a letra 3
