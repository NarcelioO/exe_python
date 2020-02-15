l1 = float(input("Digite lado1: "))
l2 = float(input("Digite lado2: "))
l3 = float(input("Digite lado3: "))

if (l1 > (l2+l3)) and (l1 < round(l2-l3)):
    print("N vai da n")

if  (l2 > (l1+l3)) and (l2 < round(l1-l3)):
    print("N vai da n")

if  (l3 > (l2+l1)) and (l3 < round(l1-l2)):
    print("N vai da n")
else:
    print("Da sim po")