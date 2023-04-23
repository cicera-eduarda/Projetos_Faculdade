#Façã um algoritmo que leia o preço de um produto e mostre seu novo preço com 5%de desconto

a = float(input('Digite o valor do produto: R$:'))
b = (a-(a*(5/100)))
c = (a - (a*(25/100)))
print('O produto de valor R${:.2f}, possui um desconto de 5% tendo um valor final de {:.2f}. Com um desconto especial de 25% {:.2f}'.format(a, b, c))

