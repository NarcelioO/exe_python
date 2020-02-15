dis = int(input("Km da viagem"))

if dis >= 200:
    preco = dis * 0.50
else:
    preco = dis * 0.45

print("Preço das Passagens: R${:.2f}".format(preco))