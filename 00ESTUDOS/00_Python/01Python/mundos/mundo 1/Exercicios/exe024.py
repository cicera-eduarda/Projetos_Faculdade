# Crie um programa que leia o nome  de uma cidade. e diga se a a cidade começa ou nao com a palavra " santo"

nome = (str(input('Insira o nome da Cidade:'))).strip()
print(nome[:6].upper()=='SANTO') ##O NOME DA CIDADE COMEÇA COM SANTO? AS CINCO PRIMEIRAS CARACT. SAO IGUAL A SANTO? mais uma caracter para 
#nao correr o risco de ser santos 

