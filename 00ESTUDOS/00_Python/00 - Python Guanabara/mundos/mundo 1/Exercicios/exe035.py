##Desenvolva um program que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um trriangulo
#Dados três segmentos de reta distintos, se a soma das
# medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.

n1=float(input('Insira o primeiro segmento: '))
n2=float(input('Insira o segundo segmento: '))
n3=float(input('Insira o terceiro segmento: '))
print('-=-'*20)
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('É POSSIVEL FAZER O TRIANGULO')

else:
    print('Não é possivel fazer o triangulo')
    
print('-=-'*20)