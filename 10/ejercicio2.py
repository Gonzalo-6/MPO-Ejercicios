#ejercicio 2

edad = int(input("Cuantos años tiene? "))

if edad >= 18 and edad <=60:
    print("Puedes entrar")
elif edad > 60:
    print("Vete a oldskoolVeterans")
elif edad < 18 and edad >= 16:
    print("Vete a kindergarden")
else:
    print("Vete a casa")    