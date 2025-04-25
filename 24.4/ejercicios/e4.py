nota = int(input("Escribe la nota que desearías sacar: "))

if nota < 5:
    print(f"{nota} es suspenso")
elif  5 <= nota < 7:
    print(f"{nota} es aprovado")
elif 7 <= nota < 9:
    print(f"{nota} es notable")
elif  9 <= nota <= 10:
    print(f"{nota} es sobresaliente")    
else:
    print("nota no valida")            