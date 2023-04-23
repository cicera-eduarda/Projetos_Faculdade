##EScreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o  valor da casa o salario
#do comprador  e em quantos anos ele vai pagar

# Calcule o valor da prestação mensal, sabendo que ela nao pode execeder 30% do salario ou entao o emprestimo sera negado.

print('Emprestimo Bancario')
valor= float(input('Insira o valor da casa:'))
salario=float(input('Qual o seu salario? '))
anos= int(input('Em quantos ANOS voce deseja quitar o Imovel: '))
parcelas = anos * 12
prestação= (valor/parcelas)

if prestação <= (salario*0.30):
    print('\033[34mEmprestimo\033[m aprovado!!O valor da prestação é de {:.2f} por mes, durante {} anos.'.format(prestação,anos))
else:
    print('EMPRESTIMO NÃO APROVADO! O VALOR DA PRESTAÇÃO {}, ULTRAPASSA 30% DO SALARIO.'.format(prestação))
print('Obrigada por cotar conosco!')