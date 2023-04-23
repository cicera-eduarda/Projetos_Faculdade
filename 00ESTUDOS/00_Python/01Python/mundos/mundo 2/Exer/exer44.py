# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# a vista dinheiro/ cheque 10%
# a vista cartao 5
# em duas vezes preço normal
# 3 vezes ou mais 20%
print(40*("*"))
print('{:=^40}'.format(' LOJA DO POVÃO '))
print(40*("*"))
a = float(input('Insira o valor do produto:'))
print('''Escolha a forma de pagamento: 
   1- A vista (dinheiro/cheque), com desconto de 10 %  
   2- Débito, com desconto de 5 %   
   3- Credito em duas vezes sem juros   
   4- Credit em parcelamento 3x ou mais, com juros de 20 %''')

b = int(input('''Qual a forma de pagamento:'''))
print('') 

if b == 1:
    total= a-(a*0.10)
    print('''
    Pagamento a vista selecionado. 
    Valor do produto {:.2f} reais, desconto de 10 {:.2f}, valor com desconto {:.2f} reais.'''.format(a,('%'),total))
elif b== 2:
    total=(a-(a*0.05))
    print('''
    Pagamento no débito com desconto de 5%, valor do produto {:.2f}, valor com desconto {:.2f} reais.'''.format(a,total))
elif b==3:
    parcela= a/2
    total = a
    print('O valor total é de {:.2f} reais, dividido em duas parcelas de {:.2f} reais.'.format(a,parcela))
elif b==4:
  #  parcelamento = str(input('Deseja parcelar em 3 ou mais vezes ?')).upper()
   # if parcelamento == 'SIM':
        numerodeparcelas = int(input('Insira o numero de parcelas:'))
        parcela = ((a*0.20)+a)/numerodeparcelas
        total = a+(a*0.20)
       
        print('O valor total do produto é {:.2f} reais, com a adição dos juros de 20%, o valor ficar {:.2f} reais, o numero de parcelas escolhido foi {}, o valor de cada parcela é {} reais.'.format(a,juros,numerodeparcelas,parcela))
else:
    total=a
    print('Opção invalida de pagamento. Tente novamente')

print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(a,total))
print('Obrigada por comprar conosco')