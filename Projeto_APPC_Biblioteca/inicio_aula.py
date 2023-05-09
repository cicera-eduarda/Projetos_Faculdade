#Dicionarios


tabela_preco = {'cadeira':250.56 , 'mesa':1234.0, 'estante':2500}
tabela_preco['sofa']=3500
print(tabela_preco)
del tabela_preco['cadeira']


for produto, preco in tabela_preco.items():
    print(f"Produto: {produto} \n Preço: {preco}")