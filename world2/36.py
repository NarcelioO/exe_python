value_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario: "))
anos = int(input("Em quantos anos pretende pagar? "))


prestaçao = value_casa / (anos*12)


if prestaçao > (salario*0.30):
    print("Desculpe, seu emprestimo foi negado.")
else:
    print('Concluido.')