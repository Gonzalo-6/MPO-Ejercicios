numero1 = int (input("Introduce un número: "))
numero2 = int (input("Introduce otro número: "))
signo = input("Introduce un simbolo de estos(+, -, *,/): ")

if signo == "+":
    resultado = numero1 + numero2
elif signo == "-":
    resultado = numero1 - numero2
elif signo == "*":
    resultado = numero1 * numero2
elif signo == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "NO se puede dividir por cero"
else:
    resultado = "Opresación no valida"  
print(f"Resultado es: {resultado}")   