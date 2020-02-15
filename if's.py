import random

choice = int(input("tente acertar o numero da maquina entre 0 e 5: "))
numero = random.randint(0,5)

if choice==numero:
    print("vc acertou")
else:
    print("ERROU")

print(numero)