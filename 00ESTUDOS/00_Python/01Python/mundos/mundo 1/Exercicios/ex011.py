#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pinta - la
#Sabendo que cada litro de tinta pinta uma area de 2 m²
Alt = float(input('Insira a altura da parede em metros:'))
Larg = float(input('Insira a largura da parede em metros:'))
área = Alt*Larg
tinta = área / 2 
print('A parede de {} x {} possui {} metros quadrados, para pinta-la são necessarios {} litros de tinta'.format(Alt, Larg, área, tinta))