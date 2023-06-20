#Computador pensa em um numero entre 0 e 10. So que agora o jogador 
#vai tentar adivinhar ate acertar. mostrando no  final quantos palpiter foram 
#necessarios para vencer.

from random import randint
from time import sleep

tentativa=1
computador = randint(0,10)
print("Pensando em um numero...")
sleep(1)

jogador=int(input("Digite qual numero o computador pensou? "))

while jogador!=computador:
    jogador=int(input("Puxa... Não foi dessa vez! Tente outro numero!: "))
    tentativa+=1

print(f"Parabens! Voce acertou! O numero pensado foi {computador} e você escolheu {jogador} em sua {tentativa}º tentativa")

