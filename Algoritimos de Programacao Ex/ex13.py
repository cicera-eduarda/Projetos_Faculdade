num = int(input("Digite um numero: "))


if num <=1:
    print("Não é primo")
else:
    for i in range(2,num):
        if num%i==0:
            print("Nao é primo")
            print(i)
            break

    else: print("é primo")


