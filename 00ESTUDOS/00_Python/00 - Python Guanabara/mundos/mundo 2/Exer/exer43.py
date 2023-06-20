# desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acorodo com a tabela abaixo:
# abaixo de 18.5 abaixo do peso
# 18,5 e 25 peso ideal
# 25 ate 30 sobrepeso
#30 ate 40 obesidade
#acima de 40 obsidade morbida
print(20*"*")
print('     Calulo IMC')
print(20*"*")
peso= float(input('Insira o peso em kg:'))
altura= float(input('Insira a altura em metros:'))
altura1= altura*altura
#altura**2
imc = peso/altura1

if imc < 18.5:
    print('Abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print("""Parabens você esta na faixa de peso ideal! 
    Peso ideal""",)
elif 25 <= imc < 30:
    print('Sobre peso')
elif 30 <= imc < 40:
    print('Obsidade')
else:
    print('OBSIDADE MORBIDA')

print('Em caso de duvida procure um medico especializado')