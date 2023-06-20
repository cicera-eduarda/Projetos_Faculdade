###         Estruturas de controles     ###

##          Lações de Repetição         ###
##                  FOR                 ###

for c in range (1,6): # UM ATE 5 NAO CONSIDERA O ULTIMO NUMERO
    print('oi')
print('FIM')

for c in range (0,6):
    print(c)
print('FIM')

for c in range (0,7):
    print(c)
print('FIM')

for c in range (6,0,-1): ## CONTAGEM PARA TRAS DIZER QUAL É A ITERAÇÃO
    print(c)
print('FIM')

for c in range (0,7,2): # PULANDO DE DOIS EM DOIS
    print(c)
print('FIM')


N = int(input('Digite um numero:'))
for c in range (0, N+1):
    print(c)
print('fim')


i = int(input('inicio:'))
f = int(input('fim:'))
p = int(input('passo:'))

for c in range (i, f+1, p): #sempre para um antes
    print(c)
print('Fim')


## vou solicitar tres vezes o valor
for c in range (0,3):
    n = int (input('Digitre um valor:'))
print('fim')

s = 0
for c in range (0,4):
    n = int(input('Digite um valor'))
    s += n
print('A somatoria de todos os valores foi {}'.format(s))


print ('-'*20)
print("Contando elementos")
for _ in "let's code":
  print("Olá, mundo!")

print("Multiplicação de elemento por numero")
for _ in " "*10:
    print("Olá, mundo!")

print("Range")
for _ in range(10, 20, 1):
    print("Olá, mundo!")

print("Multiplicação por lista")
for _ in [10]:
    print("Olá, mundo!")

print("Multiplicação de lista por elemento")
for _ in [10]*10:
    print("Olá, mundo!")