mes = input("Intruduce un mes para saber cuantos días tiene: ").lower()
if mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]:
    print(f"{mes.capitalize()} tiene 31 días")
elif mes in ["abril", "junio", "septiembre", "noviembre"]:
    print(f"{mes.capitalize()} tiene 30 días")
elif mes in ["febrero"]:
    print(f"{mes.capitalize()} tiene 28 días")
else:
    print("Mes no valido")
        