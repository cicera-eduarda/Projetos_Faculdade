# crie um programa que leia duas notas de um aluno e calcule sua media mostrando uma mensagem no final, de acordo com a media atingida
#media abaixo de 5: reprovado
#media entre 5 e 6,9 recuperação
#media 7 ou superior aprovado




print('Calculadora de Medias')
a=(str(input('Insira o nome do aluno:')))
n1=(float(input('Insira a primeira nota do aluno:')))
n2=(float(input('Insira a segunda nota do aluno:')))
media=(n1+n2)/2

if media < 5:
    print('Reprovado, {} media menor que 5.'.format((n1+n2)/2))
elif 5 <= media < 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')

b = (input('Assine abaixo para dar ciencia:'))

if a == b:
    print('obrigada')
else:
    print('Informe o nome corretamente')
    