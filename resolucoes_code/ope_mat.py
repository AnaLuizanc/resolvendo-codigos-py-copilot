# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

number1 = float(input("Enter float: "))
number2 = float(input("Enter float: "))

print("Sum: ", number1+number2)
print("Subtraction: ", number1-number2)
print("Multiply: ", number1*number2)
if number2 != 0:
    print("Division: ", number1/number2)