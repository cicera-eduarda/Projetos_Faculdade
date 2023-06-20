# refaça o exercicio 35 acrescentando o recurso de mostrar que tipo de triangulo sera formado
# equilatero, isosceles, escaleno
##Desenvolva um program que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um trriangulo
#Dados três segmentos de reta distintos, se a soma das
# medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.

n1=float(input('Insira o primeiro segmento: '))
n2=float(input('Insira o segundo segmento: '))
n3=float(input('Insira o terceiro segmento: '))

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
      print("Estes segmentos podem formar um triângulo ", end='')
      if n1 == n2 ==n3:
            print("Equilatero")
      elif n1 != n2 != n3 != n1: #n1 e n2 podem ser diferentes mais não iguais a n3
            print("Escaleno")
      else:
            print("Isoceles")
else:
      print("Os segmentos não formam um triangulo")