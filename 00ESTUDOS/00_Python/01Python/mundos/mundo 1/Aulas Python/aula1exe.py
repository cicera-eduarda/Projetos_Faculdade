#nome = input ('Qual seu nome?') #nome recebe input qual o seu nome
#idade = input ('Quantos anos você tem?')
#peso = input ('Qual seu peso?')
#print(nome, idade, peso)

#script para dados iniciais

#nome2 = input ('Qual seu nome?') 
#print('Seja bem vindo!', nome2)
#idade2 = input ('Qual seu dia de nascimento?')
#idade3 = input ('Qual seu mês de nascimento?')
#idade4 = input ('Qual seu ano de nascimento?')
#print('Você nasceu no dia', idade2, 'de', idade3, 'de', idade4,'.', 'Correto?')





numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite o segundo número:'))
soma=numero1+numero2
cores = {'limpa':'\033[m',
'cor1':'\033[;032m',
'cor2':'\033[;34m'}
print('A soma dos dois números é {}{}{}.'.format(cores['cor1'],soma,cores['limpa']) )
print('A soma dos números é {}{}{}.'.format(cores['cor2'],(numero1+numero2),cores['cor2']))
