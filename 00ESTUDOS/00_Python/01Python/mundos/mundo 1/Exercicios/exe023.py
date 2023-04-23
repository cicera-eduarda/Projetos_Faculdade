#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# exe o numero é 1834
#unidade:4 
#dezena: 3
#centena: 8 
#milhar: 1

n = (int(input('Insira um número de 0 a 9999:')))
u = n % 10 ##tem como resto 2 ## divido por 1 e depois divido por 10 pegando o resto da divisao que é o numero depois da virgula
d = n//10 % 10 ##divido por 10 pego o resultado inteiro e divido por 10 pegando o resto
c = n //100 % 10
m = n //1000 % 10
print('A unidade é {}'.format(u))
print('A dezena {}'.format(d))
print('A centena é {}'.format(c))
print('O milhar é {}'.format(m))

#print('unidade: {}'.format(n[3])) ##So funciona com 1000 para cima
#print('dezena: {}'.format(n[2])) 
#print('centena: {}'.format(n[1]))
#print('milhar: {}'.format(n[0]))


