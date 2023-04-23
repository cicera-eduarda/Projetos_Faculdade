# + adição - subtração *vezes /divisão ** potencia // divisão inteira %modulo ou resto de divisão 

print(5+2) 
print(5-2)
print(5*2)
print(5/2) ##Numero flutuante
print(5**2)
print(5//2)## divisão inteira
print(5%2) ## resto da divisão

#                                            ##Ordem de precedencia Conversão Aritimetica ####                                        
##Ordem de precedencia deles (((1- parenteses 2- ** potencias 3 - * / // % faz quem aparecer primeiro 4 - + e -)))

print(5+3*2)
print(5+(3*2))
print((3*5)+(4**2))
print(3*(5+4)**2)## resultado errado sempre que colocar parentesees vai realziar primeiro

nome = input('Qual seu nome?')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome)) ##20 CARACTER
print('Prazer em te conhecer {:<20}!'.format(nome)) #Caracter no começo
print('Prazer em te conhecer {:>20}!'.format(nome))#Caracter no final das 20
print('Prazer em te conhecer {:^20}!'.format(nome))#Centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor:'))
n2 = int((input('Outro valor:')))
print('A soma vale {}'.format(n1+n2))
s= n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma vale {}!'.format(s))
print('A multiplicação {}!'.format(m))
print('A divisão vale {}'.format(d))
print('A divisão inteira vale {}'.format(di))
print('A exponencial vale {}'.format(e))
print('A soma é {}, a multiplicação é {}, a divisão vale {:.3f} e a exponencial é {}.'.format(s,m,d,e), end='') ## continua na mesma linha end=''
print('A divisão inteira é {}, o valor exponencial é  {}'.format (di, e))

print('A soma é {},\n a multiplicação é {},\n a divisão vale {:.3f}\n e a exponencial é {}.'.format(s,m,d,e)) ##nova linha \na
print('A divisão inteira é {}, o valor exponencial é  {}'.format (di, e))