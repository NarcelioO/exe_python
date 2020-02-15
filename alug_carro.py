km = float(input("Km rodados: "))
dias = int(input("dias alugado: "))

preco = (dias * 60) + (km * 0.15)

print("Preço a pagar: {}".format(preco))