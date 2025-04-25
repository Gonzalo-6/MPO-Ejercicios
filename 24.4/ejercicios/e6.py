año = int(input("Introduce un años para saber si es bisiesto: "))

if año %4 == 0:
    print(f"{año} es bisiesto.")
else:
    print(f"{año} no es bisiesto.")   