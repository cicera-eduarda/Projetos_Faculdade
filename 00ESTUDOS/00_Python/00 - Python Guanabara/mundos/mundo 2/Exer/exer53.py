#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
#desconsiderando os espaços

frase= input("Escreva sua frase: ").strip().upper() #tirar espacos começo e final, colocar como maiuscula
palavras= frase.split() #separacao da fase em palavras/dividir
junto =''.join(palavras)#agrupar todas as palavras onde houver determinada caracteristica 
inverso=''

for letra in range(len(junto)-1,-1,-1): 
    inverso+=(junto[letra])
#para cada letra do intervalo (contado(len)) da frase faça
#percorra cada letra do total -1, ate -1 (para em 1), de -1 em -1 (de letra em letra)
#cicera -> 6 letras index começa no zero, por isso tiramos -1 -> 0ao5 letras
if inverso==junto:
    print(junto,'=',inverso)
    print("é um palindromo")
else:
    print(frase)
    print("Nao e um palindromo")






