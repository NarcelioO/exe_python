velo = int(input("Velocidade constatada: "))
multa = (velo-80)*7
if velo > 80:
    print("Voce ultrapassou o limite, sua é multa é de: R${}.".format(multa))
else:
    print("tudo ok")