print ("Sistema para calcular el promedio de un alumno.")

nombre = input("Cual es tu nombre?: ")

matematicas = int(input(nombre + " cual es tu calificacion en matematicas?"))
quimica = int(input(nombre + " cual es tu calificaion en quimica?"))
biologia = int(input(nombre + "caul es tu calificacion en biologia?"))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 6: 
    print(nombre + " felicidades aprobaste con un promedio de:", promedio)

else:
    print(nombre + " tu promedio es de:", promedio, "no has aprobado")

print("Fin.")

    
