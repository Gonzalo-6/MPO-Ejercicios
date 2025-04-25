#Ejerciccio 4

print("Ejercicio 4: Multiplos de 3 y 5")
numero1 = int(input("Introduce un número entero: "))

if numero1 % 3 == 0 and numero1 % 5 == 0:
    print(f"{numero1} es multiplo de 3 y 5")
elif numero1 % 3 == 0:
    print(f"{numero1} es multiplo de 3")  
elif numero1 % 5 == 0:
    print(f"{numero1} es multiplo de 5")
else:
    print(f"{numero1} no es multiplo de 3 ni de 5")        