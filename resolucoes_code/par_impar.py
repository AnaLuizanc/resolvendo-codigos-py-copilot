# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

number = int(input("Enter an integer: "))

if number%2 == 0:
    print(number, "is pair.")
else:
    print(number, "is odd.")