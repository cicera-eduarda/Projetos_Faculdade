# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com
# a idade
# ate 9 anos : miri
# ate 14 anos: infantil
#ate 19 anos: junior
# ate 20 anos : senio
#acima master

print('*-*'*20)
print('           CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('*-*'*20)
nome=(str(input('Insira o nome completo do atleta:')))
idade=(int(input('Insira a idade em anos do atleta:')))

if idade < 9:
    print('{} o atleta se encaixa na categoria: MIRIM'.format(nome))
elif 9 <= idade < 14: ## idade > 92111
    print('{} o atleta se encaixa na categoria: INFANTIL'.format(nome))
elif 14 <= idade < 19:
    print('{} o atleta se encaixa na categoria: JUNIOR'.format(nome))
elif 19 <= idade < 25:
    print('{} o atleta se encaixa na categoria: SENIOR'.format(nome))
else:
    print('{} o atleta se encaixa na categoria: MASTER'.format(nome))

print('boa competição!')
