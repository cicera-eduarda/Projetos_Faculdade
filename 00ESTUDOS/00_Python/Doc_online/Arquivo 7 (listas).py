##Mais Sobre listas

fruits = ['orange','apple','pear','banana','kiwi','apple','banana']     ###list.count(nome do item) conta quantos itens deste valor tem 
print(fruits.count('apple'))
print(fruits.count('tangerina'))
print(fruits.index('banana'))
print(fruits.index('banana',1))                                     ###list.index(nome do item, após a posição x) retorna a posição que o item esta
print(fruits.index('banana',4))
print(fruits.index('apple',2))                                         ### buscar 'apple' na lista frutas apartir do item 2, retornando a posição 5
print(fruits)
fruits.reverse()                                                        ##Reverse a posição dos itens da lista
print(fruits)
fruits.append('grape')                                                 ### adiciona um item ao final da lista 
print(fruits)
fruits.sort()                                                           ### personaliza a ordenação da lista
print(fruits)
print(fruits.pop())                                              ## remove o item de uma dada posição na lista e o retorna. se nao for escolhido vai ser o utlimo
fruits.pop() 
print(fruits)

##Ultimo a entrar, primeiro a sair[]

##para adicionar um item aO TOPO DA LISTA UTILIZE APPEND() para um item do topo da lista use pop()
stack=[3,4,5]
(stack.append(6)) #adicionar item a lista por ultimo
print(stack)  
print(stack.pop()) ## ultimo item adicionado na lista retorno e retirar item
print(stack)
stack.pop() ##retirar item da lista ultimo listo
print(stack)
stack.pop() #retirar ultimo item da lista
print(stack)

##primeiro a entrar, primeiro a sair
from collections import deque
from traceback import print_tb
queue = deque (["eric","john","michael"])
print(queue)
queue.append("terry") #adicionar item, terry chegou
queue.append("graham") #adicionar item, graham chegou
print(queue)
queue.popleft()  ## o primeiro a chegar vai embora
print(queue)
queue.popleft() ##o segundo vai embora
print(queue) 

#Criar listas
squares=[]
for x in range(10):
   squares.append(x**2) ##adicionar item ao final da fina
print(squares)
##outra maneira
squares1 = list(map(lambda x: x**2, range(10)))
print(squares1)
##outra maneira
squares2 = [x**2 for x in range(10)]
print(squares2)

##Combinação de elementos de uma lista

print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y])
## x e y fazem parte de um conjunto. Para x temos 1,2,3 e para y 3,1,4 
## se x é diferente de y.
## outra maneira
combs = []
for x in [1,2,3]:
   for y in [3,1,4]:
      if x !=y:
         combs.append((x, y))

print(combs)

vec = [-4, -2, 0, 2, 4]
##criando outra lista com o dobro dos valores
#multiplicar por dois os valores de x na lista vec
print([x*2 for x in vec])
#filtrar a lista excluindo os numeros negativos
print([x for x in vec if x>= 0])

##aplicar uma função em todos os elementos #abs retorna o valr absoluto
print([abs(x) for x in vec])

##chamada de um metodo por elemento
freshfruit = ['banana', 'loganberry', '   passion fruit']
print([weapon.strip() for weapon in freshfruit]) ##sem os espaço

##criar uma lista de dupla contendo o numero e seu quadrado

print([(x, x**2) for x in range(6)])
#para a equação descrita x na sequencia determinada

##Unir uma lista usando for
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem]) ## nao entendi

for elem in vec:
   for num in elem:
      print(num)

#print(num.si for num in vec) ## nao entendi
print('oi')

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])
##arredondar pi com o numero de casas igual a i sendo i estando dentro do intervalo 

##Matrizes matematicas

matrix = [[1,2,3,4],
[5,6,7,8],
[9,10,11,12]]
print([[row[i] for row in matrix] for i in range(4)]) ##transpor as colunas para linhas
###ou
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

##ou
print(list(zip(*matrix)))
