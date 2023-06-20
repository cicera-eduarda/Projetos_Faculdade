##EScreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
## Para salarios superiores a 1250 calcule um aumento de 10
##Para os inferiores ou iguais o aumeto é de 15 %

salario= float(input('Qual o valor do salario? '))
n = ((salario*0.10)+salario) # valor do salario com aumento 10%
n1 = ((salario*0.15)+salario) # valor do salario com aumento de 15%

if salario >= 1250:
    print(f'O funcionario recebera {n-salario} reais de aumento, totalizando {n} reais')
else:
    print(f'O funcionario recebera {n1-salario } reais de aumento, totalizando {n1} reais')