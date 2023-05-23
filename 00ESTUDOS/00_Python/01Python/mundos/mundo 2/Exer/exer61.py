#REFACA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZAO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSAO USANDO A ESTRUTURA WHILE


# Pa é a sequencia numeria cada por uma razao constante a um numero ex: 1termo 10 razao 2 = 10 12 14 16 18 20
print(f'{"Gerardor de PA":^40}')
print('-'*40)
primeiro=int(input("Insira o primeiro termo da PA: "))
razao = int(input("Insira a razao da PA: "))
termo = primeiro # o primeiro termo é o numero digitado
c = 1
total_termos=0
mais_termos = 10

while mais_termos >=1:

    total_termos=total_termos+mais_termos

    while c <=total_termos: #enquanto c menor ou igual a 10 faz o loop
        #demais termos
        print(f"{termo} -> ", end='')
        termo+=razao
        c+=1
    print("Pausa")
    mais_termos=int(input("Digite quantos termos você quer mostrar a mais: "))

print(f"Progressao finalizada com {total_termos}")





