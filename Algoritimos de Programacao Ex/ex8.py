while True:
    elementos = int(input("Digite a quantidade de elementos ate 20: "))
    if elementos<20:
        break
    else:
        print("Insira um numero valido!")

lista=[]

for i in range (elementos):
    
    elemento=(int(input(f"Digite o o elemento {elementos} da lista:")))
    lista.append(elemento)
    elementos-=1
    
    lista2=[]

#for elemento in lista:
    if lista[i]%3==0:

    #if elemento%3==0:
        lista2.append(lista)

print(f"Elemento multiplo de 3 {lista2}")


