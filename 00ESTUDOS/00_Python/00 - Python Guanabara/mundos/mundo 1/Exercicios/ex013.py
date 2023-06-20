#Programa para calcular reajuste de funcionario com 15% de aumento
a = float(input('Qual o salario do funcionario: R$'))
b = (a + (a * (15/100)))
print('O funcionario que ganhava R${:.2f}, passa a ganhar com 15%, de aumento o valor de R${:.2f}.'.format(a, b))
