print("Sistema vacacional de RAPPI. \n")

nombre = input("Nombre del empleado:")

print("\nA continuacion escriba uno de los siguientes claves sabiendo que:")
print("1) Atencion al cliente")
print("2) Logistica")
print("3) Gerencia\n")

clave = int(input("Numero de clave:"))

if clave >= 4:
    print("La clave no existe")

else:
    años = int(input("\nAños de servicio de " + nombre + ":"))

if clave == 1:
    print("\n-Empleado de atencion al cliente-")
    if años == 1:
         print(nombre + " 6 dias de vacaciones")
    elif años == 2 or años == 3 or años == 4 or años == 5 or años == 6:
            print(nombre + " 14 dias de vacaciones")    
    elif años >= 7:
                print(nombre + " 20 dias de vacaciones")
    elif años == 0:
                 print(nombre + " sin derecho a vacaciones")

if clave == 2:
    print("\n-Empleado de logistica-")
    if años == 1:
         print(nombre + " 7 dias de vacaciones")
    elif años == 2 or años == 3 or años == 4 or años == 5 or años == 6:
            print(nombre + " 15 dias de vacaciones")    
    elif años >= 7:
                print(nombre + " 22 dias de vacaciones")
    elif años == 0:
                 print(nombre + " sin derecho a vacaciones")

if clave == 3:
    print("\n-Empleado de la gerencia-")
    if años == 1:
         print(nombre + " 10 dias de vacaciones")
    elif años == 2 or años == 3 or años == 4 or años == 5 or años == 6:
            print(nombre + " 20 dias de vacaciones")    
    elif años >= 7:
                print(nombre + " 30 dias de vacaciones")
    elif años == 0:
                 print(nombre + " sin derecho a vacaciones")
            
print("\nFin del programa")

