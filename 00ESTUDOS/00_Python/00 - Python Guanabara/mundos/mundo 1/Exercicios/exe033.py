##faça um programa que leia tres numeros e mostre qual o vaior e qual o menor 
n = int(input('Insira o primeiro numero:'))
n2 = int(input('Insira o segundo numero:'))
n3 = int(input('Insira o terceiro numero:'))
num = [n,n3,n2]
max= max(num)
min = min(num)
print( 'O maior numero é:{}'.format(max))
print( 'O menor numero é: {}'.format(min))

menor = n
if n2<n and n2<n3:
    menor = n2
if n3<n and n3<n2:
    menor = n3

maior = n 
if n2>n and n2>n3:
    maior = n2

if n3>n and n3>n2:
    maior = n3

print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
#if n<n2:
   # print('O numero {} é o menor da lista'.format(n))

##  if n<n2 and n<n3:
    #menor = a
##if n2<n3 and n2<n:
# menor = b
## if n3<n and n3<n2:
# menor = c