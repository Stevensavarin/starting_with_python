print("=========")
print("Conversor")
print("========= \n")

print("Menu de opciones: \n")
print("Presiona 1 si deseas convertir de numero a palabra")
print("Presiona 2 si deseas convertir de palabra a numero \n")

opcion = int(input("Cual es tu opcion deseada?:"))

if opcion == 1:
    print("\n Convertidor de numero a palabra \n")

    opcion_uno = int(input("Cual es el numero que deseas convertir a palabra?: "))

    if opcion_uno == 1:
        print("El numero es Uno")
    elif opcion_uno == 2:
        print("El numero es Dos")
    elif opcion_uno == 3:
        print("El numero es Tres")
    elif opcion_uno == 4:
        print("El numero es Cuatro")
    elif opcion_uno == 5:
        print("El numero es Cinco")
    else:
        print("El numero seleccionado no esta registrado")

elif opcion == 2:
    print("\n Convertidor de palabra a numeros \n")

    opcion_dos = input("Cual es la palabra que deseas convertir a numero?: ")
    opcion_dos = opcion_dos.lower()

    if opcion_dos == "uno":
        print("El numero es 1")
    elif opcion_dos == "dos":
        print("El numero es 2")
    elif opcion_dos == "tres":
        print("El numero es 3")
    elif opcion_dos == "cuatro":
        print("El numero es 4")
    elif opcion_dos == "cinco":
        print("El numero es 5")
    else:
        print("El numero seleccionado no esta registrado")
        
else:
    print("Esta opcion no esta disponible")

print("Fin.")
