n = 1
par = impar =0
while n != 0:
    n = int(input("Digite um numero inteiro: "))
    if n % 2 ==0:
        par += 1
    else:
        impar += 1

print("Voce digitou {} numero pares e {} numeros impares.".format(par, impar))