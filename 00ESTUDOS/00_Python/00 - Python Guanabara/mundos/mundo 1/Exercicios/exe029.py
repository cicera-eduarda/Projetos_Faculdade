##Escreva um programa que leia a velocidade de um carro 
##se ele ultrapassar 80 mostre uma mensagem dizendo que ele foi multado
## a multa vai custar 7 por cada km acima do limite

v=int(input('Insira a velocidade do carro em quilometros:'))
velocidade = (v-80)
multa = ((v-80)*7)
if v > 80:
    print('Você esta acima do limite de velocidade {}km! O Valor a ser pago é de {}'.format(velocidade,multa))

print('Parabens sua velocidade é {}, voce esta dentro da velocidade permitida'.format(v))
