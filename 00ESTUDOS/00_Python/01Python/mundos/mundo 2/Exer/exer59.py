#Crie um programa que leia dois valores e mostre um menu na tela
#[1]Somar
#[2]Multiplicar
#[3]Maior 
#[4]Novos numeros
#[5]Sair do programa
#O programa devera realizar a operação solicitada em cada caso

print("Insira os valores desejados para obtenção das operações\n")
primeiro=int(input("Insira o primeiro valor: "))
segundo=int(input("Insira o segundo valor: "))
opc=0

while opc!=5:
    print("-------Menu-------")
    print("[1]SOMAR\n[2]Multiplicar \n[3]Maior\n[4]Novos Numeros\n[5]Sair do programa ")
    opc=int(input("Digite a opção desejada: "))

    if opc==1:
        print("Operaçaõ de Soma")
        soma=primeiro+segundo
        if primeiro>segundo:
            maior=primeiro
        else:
            maior=segundo
        print(f"O maior valor é {maior}")

        print(f"O valor da soma é {soma}\n")
    elif opc==2:
        print("Operação de Multiplicação")
        mult=primeiro*segundo
        print(f"O valor desta operação é {mult}\n")
    elif opc==3:
        print("Operacao de Divisao [primeiro/segundo]\n")
        if segundo==0:
            print("Impossivel dividir por zero!\n")
        else:
            div=primeiro/segundo
            print(f"O valor da operação é {div}\n")
    elif opc==4:
        print("Inserção de novos numeros: ")
        primeiro=int(input("Insira o novo numero: "))
        segundo=int(input("Insira o segundo numero: "))
        print(f"Os novos numeros sao {primeiro} e {segundo}")
    elif opc==5: # ele ja sai do loop quando digitado 5, mas cai tambem em opção invalida!
        break
    else:
        print("Digite uma opção valida!")
    