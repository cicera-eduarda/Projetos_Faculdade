squares= [1,4,9,16,25]
#print(squares)
print(squares[:4])
print(squares[-3:])
print(squares[:-3])
squares= squares+[36,49,64,81,100]  #adição de mais numeros a lista
print(squares)
cubes=[1,8,27,65,125] #substituir itens em listas
print(cubes)
cubes[3]=64            #substituição de item errado 
print(cubes)
## APPENDE ## ADIÇÃO DE ITENS NO FINAL DA LISTA
cubes.append(216) ## adição do cubo de 6
cubes.append(7**3) # adição do cubo de 7
print(cubes)
cubes.append(5)
##CONTAGEM DO TAMANHO DA STRING
S='EBAAAAAA'
len(S)
print(len(S))
##quantidade de numeros em uma lista
a=[1,2,3]
len(a)
print(len(a))
##ALTERAÇÃO DO TAMANHO DAS LISTAS##

letters = ['a','b','c','d', 'e','f','g']
print(letters)
letters[2:5]##TRECHO DETERMINADO
print(letters[2:5])
letters[3:5]=['C','D','E']##SUBTITUIÇÃO DE ITENS NA LISTA
print(letters)

## SOMA E SUBTRAÇÃO LISTAS
letters[2:5]=[]
print(letters)

##Criando lista em outras listas
a=['a','b','c']
n=[1,2,3]
x=[a,n]
print(x)
print(x[0][1])


a, b = 0, 20
while a < 400 : # retirar jogo da velha para usar
 print(a,end=',')  ##end pode ser usado para evitar a criação de uma nova linha 
 a,b=b,a+b

 
## W h i l e - enquanto determinada condição ocorrer 
###a soma de dois elementos definidos
#a,b=0,1
#while a<10:
 #   print (a)
  #  a,b=b, a+b
## WHILE E PRINT
i= 256*256
print('The value of i is',i)

a, b = 1,20
while a < 10 : # retirar jogo da velha para usar
 print(a,end=',')  ##end pode ser usado para evitar a criação de uma nova linha 
 a,b=b,a+b

##COMANDO IF

x=int(input("Please enter an integer:"))  ##INSERIR VALOR DE 0 1 -1 OU 42 NA RESPOSTA DO TERMINAL
if x < 0:
    x=0
    print('Negative changed to zero')
elif x== 0:
        print('Zero')
elif x == 1:
            print('Single')
else:
                print('More')

##COMANDO FOR ##
words = ['cat','window','defenestrate']
for w in words:
    print(w,len(w))

for B in range(5):
    print(B)
    