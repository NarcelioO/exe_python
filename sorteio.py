import random

alu1 = input("Digite um nome: ")
alu2 = input("Digite um nome: ")
alu3 = input("Digite um nome: ")
alu4 = input("Digite um nome: ")

alunos = [alu1,alu2,alu3,alu4]
                  #escolhe

escolhido = random.choice(alunos)
print(escolhido)

#random.shuffle (Embaralha)