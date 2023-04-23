##Sequencias numericas 
##range(stop) primeira definição ou definição simplificada
##range ([start], stop[,step])segunda definição ou definição completa
##o inicio da sequencia, o utilmo elemento, o intervalo entre cada elemento
##range gera progressoes aritmeticas
from typing import Match


print(list(range(2,40,3)))

for B in range(5):
    print(B)  ## Intervalo aberto em nao conntendo  5

print(list(range(5,10))) 
print(list(range(0,10,3)))
print(list(range(-10,-100,-30)))
print(list(range(2,10)))
print(list(range(0,-10,-1)))
print(range)

#a= ['Mary','had','a','little','lamb']
#for i in range (len(a)):
 #   print(i,a[i])
#print(sum(range(4)))

##Sequencia com numeros primos 



for n in range (2,10):
    for x in range(2,n):
        if n % x == 0: ##Se o resto da divisão for zero o número não é primo.
            print(n, 'é igual', x, '*',n//x)   #n é igual a um numero do intervalo x é igual ao primeiro numero do intervalo
            break
    else:
            ## loop fell through without finding a factor
            print(n, 'é um numero primo')  ##Se nenhum resto for zero, o número é primo.


for n in range (2,20):
    for x in range(2,n):
        if n % x == 0:
            print (n, 'é igual',x, '*',n//x)
            break #quebrar em
    else:
        print(n, ' é um numero primo')
    
    ##o comando else pertence ao lado for e nao ao comando if

    #agrupar tudo isso em uma coleção e fazer ele me retornar somente os numeros primos
    #quantos numeros primos existem neste intervalo


##  Numeros Pares e Impares ##
for num in range(1,10):
    if num  % 2 == 0:
        print ("Encontrou um numero par", num)
        continue
    print ("Encontrou um numero impar",num)
    
    

## Instruções match pega uma expressão e compara seu valor com padroes sucessivos fornecidos como um ou mais blocos de case 


#def http_error(status):
  #  match status:
   #     case 400:
    #        return "Bad request"
     #   case 404:
      #      return "Not found"
       # case 418:
        #    return "I'm a teapot"
        #case _:   ## _ atua como coringa e nunca falha em responder
         #   return "Something's wrong with the internet"

#case 401 | 403 | 404:
 #   return "Not allowed"

## Ponto é um (x,y) tuple

#match point:
   # case (0,0):
    #    print ("Origin")
   # case (0,y):
   #     print (f"Y={y}")
   # case Point(x=x, y=0):
   #     print (f"X={x}")
   # case Point ():
   #     print ("Somwhere else")
   # case _:
   #     print("Not a point")


##não  funciona olha que alegria
