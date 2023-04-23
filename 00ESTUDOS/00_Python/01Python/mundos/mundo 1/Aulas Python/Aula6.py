#Tipos Primitivos e Saidas de dados
from xmlrpc.client import boolean


n1 = int(input('Digite um número:')) #n recebe um numero inteiro
n2 = int(input('Digite o segundo número:'))# int transformando string em numero. ## tudo que esta dentro do int vai ser um numero inteiro
s= n1+n2 ##Concatenação
print('A soma vale',s) ##Não funciona ele junta e nao soma os numeros
print('A soma vale {}'.format(s)) ## colocar dentro dos colchetes a mascara de s4
print('A soma entre {} e {} vale {}'.format(n1,n2,s)) ##pode-se colocar {0}{1}para indentificar o numero das variaveis
print('A soma entre',n1, 'e', n2,'vale', s)
print(type(n1)) ##tipo inteiro
a= ('a') ##tipo str
print(type(a))

#int (7, -4,0) float (4.5, 4.76, -15.754, 7.0) boal(True/False) str ('Olá')

n = float(input('Digite um valor '))
print(n)
n1 = str(input('Digite um valor ')) ##Texto
print(n1)
n2 = int(input('Digite um valor ')) ##Numero inteiro
print(n2)
n3 = boolean(input('Digite um valor ')) #Tem um valor? Entao e verdadeiro
print(n3)
n4 = (input('Digite um algo '))
print(n4.isnumeric()) ##é numerico ? ou nao
n4 = (input('Digite um algo '))
print(n4.isalpha()) ##é letra ?
print(n4.isalnum()) # é alfanumerico
print(n4.isupper()) ## esta somente com  letra maiuscula ##islower minuscula 

na = int(input('Digite um número: '))
nb = int(input('Digite o segundo número: '))
nc = int(input('Digite o terceiro número: '))
sa = (na+nb+nc)
print('A soma entre {}, {} e {} é igual a {}!'.format(na,nb,nc,sa))
