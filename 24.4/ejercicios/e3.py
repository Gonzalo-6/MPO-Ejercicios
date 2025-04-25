numero = int(input("Introduce un número entero"))

if numero %3 == 0 and numero %5 == 0:
    print(f"{numero} es divisible por 3 y por 5")
else:
    print(f"{numero} no es divisible por 3 y pot 5")    