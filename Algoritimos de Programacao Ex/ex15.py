altura_chico = 1.50 # metros
altura_ze = 1.10 # metros
crescimento_chico = 0.02 # metros por ano
crescimento_ze = 0.03 # metros por ano
anos = 0

while altura_ze <= altura_chico:
    altura_chico += crescimento_chico
    altura_ze += crescimento_ze
    anos += 1

print("Zé será maior que Chico em", anos, "anos.")