## Manipulando Cadeia de texto ##

#Modos de manipulação de cadeia de caracteres "Qualquer frase"

frase = 'Curso em Video Python' ##Cada uma dessas caracteris recebe um numero, incluindo os espaços

### Fatiamento ###

frase[9] #numero do indice dentro desta string
frase[9:13] #Pegar do 9 ate o 12
frase[9:21] ##ELe pega ate o vinte, mesmo nao tendo o 21
frase[9:21:2] # Começar no nove parar no 21 e vou pulando de dois em dois
frase[:5] # ele vai começar dod inicio ate 5
frase[15:] #indiquei o inicio ate o final
frase[9::3] #inicio no nove ate o final pulando de 3 em tres


#ANALISE DE STRING

len(frase) ## qual o comprimento da frase 
frase.count('o',0 ,13) #contando por fatiamento ate 12
print(frase.count('o')) # pedindo para o programa contar quantas vezes aparece o o minusculo
print(frase.find('deo')) #onde começou o deo a posição 11
frase.find('android') #como não ha esta palavra ele vai retornar -1
'Curso' in frase # existe a palavra curso? ele me diz verdadeiro ou falso


## Transformação ##

#Não podemos mudar uma string diretamente, mas podemos mudalas atraves de ferramentas..
frase.replace('Python','Android') ##substitui por
frase.upper()#Colocar todas as letras em maiuscula
frase.lower() # Colocar todas as letras em minuscula
frase.capitalize() #joga todas as caracteristica em minuscula e deixa só a primeira letra maiuscula
frase.title() # quantas palavras tem essa string e coloca cada palavra em maiuscula
frase1 = '   Aprenda Python  '  #espaços antes ou depois
frase1.strip() # remove espaços desnecessarios
frase1.rstrip() # Remove somente os utimos espaços 
frase1.lstrip() # remove somente os primeiros espaços da esquerda

##Substituir 

frase = frase.replace('Android','Python')

## DIVISAO DE STRING 

print(frase.split()) ## feito nos espaços. Pega onde esta os espaços e quebra em string pequenas, recebendo novas indexações. Separando e criando novas listas
#pega em origens nos espaços mais possui variações que podem ser colocadas em outros elementos


## Junçao ##

'-'.join(frase)##voce vai juntar todos os elementos de frase usando esse separador



