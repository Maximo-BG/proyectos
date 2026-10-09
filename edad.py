edad = int(input("¿Qué edad tienes?"))

if edad >= 18 | edad < 21:
    print("¡Ya puedes entrar a la discoteca!")
elif edad > 18 and edad < 60:
    print("Todavía estás en tu mejor momento")
elif edad >= 21:
    print("¿Vamos a beber?")
elif edad == 17:
    print("Casi, te queda 1 año")
else:
    print("no te preocupes")

print("Fin del programa")