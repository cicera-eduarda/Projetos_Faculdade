print("Insira um numero negativo para parar")

lista_par= []
lista_impar=[]
num =0

while num>=0: 
    num = int(input("Insira um numero: "))

    if num%2==0 and num>0:
        lista_par.append(num)

    elif num%2!=0 and num>0:

        lista_impar.append(num)
    elif num <0:
        break


for num in lista_par:
    print(f"Elementos lista par {num}")

for num in lista_impar:

    print(f"Elementos lista impar {num}")


