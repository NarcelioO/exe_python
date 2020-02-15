mediaidade =0
somaidade = 0
for c in range(1, 5):
    print("--- {}ª PESSOA ---".format(c))
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Sua idade:"))
    sexo = str(input('Sexo [M/F]:')).strip()

somaidade += idade
mediaidade = somaidade/2