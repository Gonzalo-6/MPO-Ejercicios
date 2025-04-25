#ejercicio 2 cuenta atras
numero = int(input("Introduce un número:\n"))
pares = 0
for i in range(0,numero+1, 2):
    if i % 2 == 0:
        pares = pares + 1

print(f"Numeros pares: {pares}")        

