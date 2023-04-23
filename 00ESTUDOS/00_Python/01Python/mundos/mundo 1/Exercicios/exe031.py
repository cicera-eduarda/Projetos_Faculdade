##Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preoço da passagem, cobrando 0,50 por km para viagens
##ate 200 e 0,75 para viagens mais longas 
distancia=int(input('INSIRA a distancia em km:'))
preço = distancia * 0.50 if distancia <200 else distancia *0.45  ##if simplificado
print('O preço da passagem sera {}'.format(preço))

###if km<=200:
  #  print(' O valor da viagem é {}'.format(distancia*0.50))

#else:
  #  print('O valor da viagem é {}'.format(distancia*0.45))

