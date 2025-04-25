#Ejercicio 4 factorial
numero = int(input("Introduce un número:\n"))
factorial = 1
for i in range(numero,1, -1):
    factorial = factorial * i
print(f"El factorial de {numero} es {factorial} ")    