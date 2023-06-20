##Primeira Fase

##Entradas Dados

print(f'\n{"Classificacao da Qualidade do AR":^40}')

while True:
    print("\nInsira os parametros solicitados abaixo: \n")
    try:
        MP10= float(input("Insira o valor de particulas inalaveis (MP10): "))
        MP25 = float(input("Insira o valor de particulas finas (MP2.5): "))
        O3 = float(input("Insira o valor do ozonio (O3): "))
        CO = float(input("Insira o valor do monoxido de carbono (CO): "))
        NO2 = float(input("Insira o valor do dioxido de nitrogenio (NO2): "))
        SO2 = float(input("Insira o valor do dioxido de enxofre (SO2): "))
    except:
        print(f"\n{'ERRO!':^40}")
        print(f"{'Insira apenas numeros!':^40}")
        
    if MP10<0 or MP25<0 or O3<0 or CO<0 or NO2<0 or SO2<0:
        print("\nInsira apenas valores positivos!") 
    else:
        break

##Classificacao do ar

print(f'\n{"Resultado":^40}')

if MP10<50 and MP25<25 and O3<100 and CO<9 and NO2<200 and SO2<20:
    print(('-')*40)
    print(f"\n{'A qualidade do ar esta BOA!':^40}")
    print(f"{'Nao a maleficios a saude!':^40}")
    print(('-')*40)
elif MP10<100 and MP25<50 and O3<130 and CO<11 and NO2<240 and SO2<40:
    print(('-')*40)
    print(f"\n{'A qualidade do ar esta MODERADA!':^40}")
    print(f"{'Pessoas de grupos sensiveis podem apresentar sintomas como tosse seca e cansaco. A populacao, em geral nao e afetada'}")
    print(('-')*40)

elif MP10<150 and MP25<75 and O3<160 and CO<13 and NO2<320 and SO2<365:
    print(('-')*40)
    print(f"\n{'A qualidade do ar esta RUIM!':^40}")
    print(f"{'Toda a populacao pode apresentar sintomas como tosse seca, cansaco, ardor nos olhos, nariz e garganta.'}")
    print(f"{'Pessoas de grupos sensiveis, podem apresentar efeitos mais serios na saude'}")
    print(('-')*40)

elif MP10<250 and MP25<125 and O3<200 and CO<15 and NO2<1130 and SO2<800:
    print(('-')*40)
    print(f"\n{'A qualidade do ar esta MUITO RUIM!':^40}")
    print(f"{'Toda a poplacao pode apresentar agravamento dos sintomas como tosse seca, cansaco,ardor nos olhos,nariz e garganta'}")
    print(f"{'e ainda falta de ar e respiracao ofegante. Efeitos ainda mais graves a saude de grupos sensiveis'}")
    print(('-')*40)

elif MP10<250 and MP25<125 and O3<200 and CO<15 and NO2<1130 and SO2<800:
    print(('-')*40)
    print(f"\n{'A qualidade do ar esta PESSIMA!':^40}")
    print(f"{'Toda a poplacao pode apresentar agravamento dos sintomas como tosse seca, cansaco,ardor nos olhos,nariz e garganta'}")
    print(f"{'e ainda falta de ar e respiracao ofegante. Efeitos ainda mais graves a saude de grupos sensiveis'}")
    print(('-')*40)                 