import math

cat_op = float(input("Digite o cateto oposto"))
cat_adj = float(input("Digite o cateto adjacente"))

calc = math.pow(cat_adj, 2) + pow(cat_op, 2)
hipot = math.sqrt(calc)



print(hipot)