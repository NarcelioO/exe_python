import math

angulo = float(input("Digite o angulo"))

seno = math.sin(math.radians(angulo))

cos = math.cos(math.radians(angulo))

tang = math.tan(math.radians(angulo))

print("Cos = {:.2f}, Sen = {:.2f}, Tan = {:.2f}".format(seno,cos,tang))