nome = input("Digite seu nome completo = ").strip()

upper = nome.upper()

lower = nome.lower()

tamanho = len(nome) - nome.count(' ')

prim_nome = nome.split()
print(upper)
print(lower)
print(tamanho)
print(len(prim_nome[0]))
