n = int(input("escolha um numero: "))
print('''esolha um das opçoes:
[ 1 ]Multiplicação
[ 2 ]adição
[ 3 ]divisão

''')
ope = int(input("Sua opcão:"))

for c in range (0, 10):
 if(ope==1):
    print("{} x {} = {}".format(n,c,n*c))
 elif(ope==2):
    print("{} + {} = {}".format(n, c, n + c))
