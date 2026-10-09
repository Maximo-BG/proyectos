def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b

# 1. Pedir los 2 números desde la terminal :)
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# 2. Imprimir los resultados directamente :c
print(f"Suma:, {num1 + num2}")
print(f"Resta:, {num1 - num2}")
print(f"Multiplicación:, {num1 * num2}")

# Validación simple para no dividir entre cero ;)
if num2 == 0:
    print("División: No se puede dividir entre cero")
else:
    print("División:", num1 / num2)




