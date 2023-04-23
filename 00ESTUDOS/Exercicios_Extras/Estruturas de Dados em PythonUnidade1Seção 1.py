texto = "Aprendendo Python na disciplina de linguagem de programação."
print(f"Tamanho do texto = {len(texto)}")
print("Tamanho do texto = {}".format(len(texto)))
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")
print(texto.upper())
print(texto.replace("i", 'XX'))
print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n")
palavras = texto.split()
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")



texto = """Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
"""
print(texto)
print(f"Tamanho do texto = {len(texto)}")
texto = texto.lower()
texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")
lista_palavras = texto.split()
print(f"Tamanho da lista de palavras = {len(lista_palavras)}")

total = lista_palavras.count("string") + lista_palavras.count("strings")

print(f"Quantidade de vezes que string ou strings aparecem = {total}")


### Listas ###

vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas

for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')


# Mesmo resultado.

vogais = []
print(f"Tipo do objeto vogais = {type(vogais)}")

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")




frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]

print("maça" in frutas) # True
print("abacate" in frutas) # False
print("abacate" not in frutas) # True
print(min(frutas)) # banana
print(max(notas)) # 10
print(frutas.count("maça")) # 2
print(frutas + notas)
print(2 * frutas)



lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "maça"]

print(f"Tamanho da lista = {len(lista)}")

for i, item in enumerate(lista):
    print(f"Posição = {i},\t valor = {item} -----------------> tipo individual = {type(item)}")

print("\nExemplos de slices:\n")

print("lista[1] = ", lista[1])
print("lista[0:2] = ", lista[0:2])
print("lista[:2] = ", lista[:2])
print("lista[3:5] = ", lista[3:5])
print("lista[3:6] = ", lista[3:6])
print("lista[3:] = ", lista[3:])
print("lista[-2] = ", lista[-2])
print("lista[-1] = ", lista[-1])
print("lista[4][1] = ", lista[4][1])


""""
##lista[1]: acessa o valor da posição 1 da lista.
lista[0:2]: acessa os valores que estão entre as posições 0 e 2. Lembre-se de que o limite superior não é incluído. Ou seja, nesse caso serão acessados os valores das posição 0 e 1.
lista[:2]: quando um dos limites não é informado, o interpretador considera o limite máximo. Como não foi informado o limite inferior, então o slice será dos índices 0 a 2 (2 não incluído).
lista[3:5]: acessa os valores que estão entre as posições 3 (incluído) e 5 (não incluído). O limite inferior sempre é incluído.
lista[3:6]: os indíces da lista variam entre 0 e 5. Quando queremos pegar todos os elementos, incluindo o último, devemos fazer o slice com o limite superior do tamanho da lista. Nesse caso, é 6, pois o limite superior 6 não será incluído.
lista[3:]: outra forma de pegar todos os elementos até o último é não informar o limite superior.
lista[-2]: o slice usando índice negativo é interpretado de trás para frente, ou seja, índice -2 quer dizer o penúltimo elemento da lista.
lista[-1]: o índice -1 representa o último elemento da lista.
lista[4][1]: no índice 5 da lista há uma outra lista, razão pela qual usamos mais um colchete para conseguir acessar um elemento específico dessa lista interna."""

###List comprehension (Compreensões de lista)


linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
#linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() # Essa sintaxe produz o mesmo resultado que a linha 1

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)



linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
print("Antes da listcomp = ", linguagens)

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()
    
print("\nDepois da listcomp = ", linguagens)



linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

linguagens_java = [item for item in linguagens if "Java" in item]

print(linguagens_java)



linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
linguagens_java = []

for item in linguagens:
    if "Java" in item:
        linguagens_java.append(item)

print(linguagens_java)



