print(" =====================================================")
print("Buenos días, soy tu asistente de cambio de moneda :)")
print(" =====================================================")
cantidad = float(input("Introduce la cantidad que quieres cambiar: "))
#tabla de conversion de monedas ;)
print(" =============================")
print ( "Elige una opcion de cambio:" )
print("1. Euros a Dolares")
print("2. Euros a Libras")
print("3. Dolares a Euros")
print("4. Libras a Euros")
print(" =============================")
opcion = int(input("Opcion (1-4): "))
#imprimo el resultado de la conversion :)
if opcion == 1:
    resultado = cantidad * 1.10
    print(cantidad, "euros son", resultado, "dolares")
elif opcion == 2:
    resultado = cantidad * 0.85
    print(cantidad, "euros son", resultado, "libras")
elif opcion == 3:
    resultado = cantidad * 0.91
    print(cantidad, "dolares son", resultado, "euros")
elif opcion == 4:
    resultado = cantidad * 1.17
    print(cantidad, "libras son", resultado, "euros")
else:
    print("Opcion no valida")
#programa de conversion de monedas finalizado :)