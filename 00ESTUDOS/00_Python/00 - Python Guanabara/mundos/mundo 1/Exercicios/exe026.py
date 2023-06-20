#Faça um programa que leia uma frase pelo teclado e mostre 
#Quantas vezes aparece a letra 'a'
#Em que posição ela aprace na primeira vez
#em que posição ela aparece a ultima vez

#Faça um programa que leia uma frase pelo teclado e mostre 
frase =(str(input('Insira a frase:'))).strip()

#Quantas vezes aparece a letra 'a'
print('A letra A aparece {} na frase'.format(frase.upper().count('A')))

#Em que posição ela aprace na primeira vez
print('A primeira letra a aparece na posição {}'.format(frase.upper().find('A'))) ## LEVANDO EM CONSIDERAÇÃ O PROGRAMA
print('A primeira letra a aparece na posição {}'.format(frase.upper().replace(' ','').find('A')+1))##LEVANDO EM CONSIDERAÇÃO A PALAVRA

#em que posição ela aparece a ultima vez
print(' A ultima letra a aparece em {}.'.format(frase.upper().rfind('A'))) ## R FIND COMECÇA PELA DIREITA com espaço QUERENDO SOMENTE APOSIÇÃO PELO PROGRAMA
print(' A ultima letra a aparece em {}.'.format(frase.upper().replace(' ', '').rfind('A'))) ## SEM ESPAÇO QUERENDO A POSIÇÃO REAL PELA PALAVRA
