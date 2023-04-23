## a intrução del
from calendar import c


a= [-1,1,2,3,4,5,6,7]
print(a)
del a[0]
print(a)
del a[2:4] ##exclusão de tres e quatro
print(a)
del a[:]
print(a) #para deletar toda a lista del a 

##Tupla, consiste em uma sequencia de valores separados por virgula ##imutavel
t = 123445, 54321, 'hello'
print(t[0])
print (t)

u= t, (1,2,3,4,5)
print(u) #vai escrever um embaixo do outro

for elem in u:
   for num in elem:
      print(num)

print([num for elem in u for num in elem])

##tupla sempre sai entre parenteses

## CONJUNTOS  SET##
#COLEÇÃO DESORDENADA DE ELEMENTOS sem elementos repetidos. usado para eliminação de itens duplicados suportando operações matematicas como 
#união intersecção diferença  e diferença simestrica

basket = {'apple', 'orange', 'apple', 'pear','orange','banana'}
print(basket) # exclui elementos duplicados 
'orange' in basket
print('orange' in basket) ##faz parte  do conjunto
print('morango' in basket) ##não faz parte do conjunto

a = set ('abracadabra')
b = set('alacazam')
print(a) ## letras unicas em a
print(a-b) # letras em a menos b
print(a|b) # letras tanto em a como em b
print(a&b) #letras em ambos os conjuntos
print(a^b) #letras em a ou b mas nao em ambos

##compreensao de listas e compreensoes de conjuntos

a={ x for x in 'abracadabra' if x not in 'abc'} ## retirar conjunto da lista
print(a)
b = { y for y in 'alacazam' if y not in 'alc'}
print(b)


###Dicionario  estrutura de dados por memoria associativa ou vetor associativo

tel= {'jack': 4098, 'sape': 4139}
tel['guido']= 4127
print(tel)
print(tel['jack'])
del tel ['sape']
tel['irv'] = 4127
print(list(tel)) ## printar em lista as chaves
print(tel)
print(sorted(tel))

print('guido'in tel) ##Guido esta em tel verdade
print( 'jack' not in tel) ##Jack nao esta em tel falso 

##o constructor dict() produz dicionarios diretamente de sequencias de pares chave-valor
print(dict([('carol',4139),('ana',3570),('paula',2630)]))
print(dict( lana=123, banana=321))

##podem ser criadas compreensões de dicionarios a partir de expressoes arbitrarias de chave e val
print({x: x**2 for x in (2,4,6)})

##Tecnicas de Iteração 
# Ao iterar sobre dicionários, a chave e o valor correspondente podem ser obtidos simultaneamente usando o método items().
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():  ##ao realizar esta açõa a chave e o valor são obtidos simultaneamente
    print(k,v)

#Enumeração de itens em dicionarios

for i, v in enumerate (['banana','maça','pera']):
 print(i, v)

#interar duas opções simultaneamente atraves de zip

question= ['name', 'quest','favorite color']
answer = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(question, answer):
    print('What is your {0}? It is {1}.'. format(q,a))

question2= ['name', 'favorite food', 'favorite color', 'favorite drink']
answer2 = ['ana','carbonara','blue','moscow mulle']
for r, b in zip (question2,answer2):
    print ('What''s your {0}? It is {1}.' .format(r,b))

##Para percorrer uma sequência em ordem inversa, chame a função reversed() com a sequência na ordem original.
for i in reversed(range(1, 100, 2)):
       print (i,end=',')

for i in reversed(range(0,100,5)):
    print(i)

##Para percorrer uma sequência de maneira ordenada, use a função sorted(), que retorna uma 
# lista ordenada com os itens, mantendo a sequência original inalterada.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana'] ##Colocou em ordem alfabetica
for f in sorted(set(basket)):
    print(f)


#numbers= [1, 20, 2, 3, 5, 4, 6, 8, 7, 9, 10, 11, 13, 12, 14, 16, 15]
#for n in sorted(set(numbers)):
  #  print(n,end=',')




## Criar uma lista nova e salvar a antiga.
# Às vezes é tentador alterar uma lista enquanto você itera sobre ela; porém, costuma ser mais simples e seguro criar uma nova lista.

##Mais sobre condições while e if podem conter quaisquer operadores, nao apenas comparações
## Comparações podem ser encadeadas por exemplo, a<b==c testa se a é menor que b e tambem que b é igual a c.
#Comparações podem ser embutidas por and e or, e o resultado de uma comparação ou de qualquer outra expressao, pode ser negado atraves de not
# A and not B or C operadores curto-circuito

string1, string2, string3 = '', '','Bolinho'
non_null = string1 or string2 or string3
print(non_null)

string1, string2, string3 = '2', '2','3' ##Paara na primeira afirmação que achar
non_null = string1 or string2 or string3
print(non_null)

#Comparando sequências e outros tipo A comparação lexicográfica de strings