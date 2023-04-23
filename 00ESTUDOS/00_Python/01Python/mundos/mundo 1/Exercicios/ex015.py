#Carro alugado. ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE Km percorridos por um carro alugado e a quantidade de dias pelos quais ele 
#foi alugado. Calcule o preço a pagar sabendo que o carro custa R$ 60 por dia e 0,15 por km rodado7
a = float(input('Quantos dias alugados?'))
b = float(input('Quantos quilometros rodados?'))
ad = 60 * a 
br = b * 0.15
total = ad + br
pago = ((a * 60) + (b * 0.15))
print('O carro alugado por {:.0f} dias e rodando por {}km, custara R${:.2f}.'.format(a, b, total))
