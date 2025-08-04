

print("Calculadora básica en Python")
print("Operaciones disponibles: +  -  *  /")


num1 = float(input("Ingresa el primer número: "))
operador = input("Ingresa el operador (+, -, *, /): ")
num2 = float(input("Ingresa el segundo número: "))


if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero"
else:
    resultado = "Operador no válido"

# Mostrar el resultado
print(f"Resultado: {resultado}")