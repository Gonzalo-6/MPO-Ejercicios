
rol = input("Dime tu rol de usuario:").lower()
academia = input("En que academia estudias o trabajas: ").lower()

if rol == "alumno" and academia == "prometeo":
    print("Puedes acceder al Discord oficial y al de alumnos")

elif rol == "profesor" and academia == "prometeo":
    print("Puedes acceder al Discord oficial")
else:
    print("No tienes acceso")    
    
