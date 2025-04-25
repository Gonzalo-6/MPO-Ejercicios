dia = input("Introduce un día de la semana: ").lower()
if dia in ["lunes", "martes", "miercoles", "jueves", "viernes"]:
    print(f"{dia.capitalize()} es laborable.")
elif dia in ["sabado", "domingo"]:
    print(f"{dia.capitalize()} es fin de semana.")
else:
    print("Día no válido.")        