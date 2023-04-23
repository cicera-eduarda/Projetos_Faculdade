##Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date

ano = int(input('Digite o ano, ou 0 para o ano atual:'))
if ano == 0:
    ano = date.today().year                            ### para pegar o ano de hoje
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto'.format(ano))
else:
    print('O ano {} não é um ano bissexto'.format(ano))