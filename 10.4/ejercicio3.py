#Pacman
#nombre_usuario - sanke_case --> Python
#nombreUsuario - camellCase --> Java

pos_pacman = int(input("Cuál es la posición de pacman?"))
pos_fantasma = int(input("Cuál es la posición del fantasma? "))

#Comprobamos que la posición de sea igual
if pos_pacman == pos_fantasma:
    #Caramelo -> Pacmana come fantasma
    #Invisible -> pacman escapa
    #Normal -> pacman atrapado
    estado_pacman = input("Como está pacman?")

    if estado_pacman == "caramelo":
        print("Pacman se ha comido al fantasma")
    elif estado_pacman == "invisible":
        print("Pacman ha escapado")    
    else:
        print("Pacman ha sido atrapado")   
else:
    print("Pacman ha escapado")
