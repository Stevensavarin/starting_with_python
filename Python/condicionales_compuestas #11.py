print("Sistema para calcular el promedio de un alumno.")

nombre = input("Cual es tu nombre?:")

matematicas = float(input(nombre + " Cual es tu calificacion en matematicas?:"))
quimica = float(input(nombre + " Cual es tu calificacion en quimica?:"))
biologia = float(input(nombre + " Cual es tu calificacion en biologia?:"))

promedio = (matematicas + quimica + biologia) / 3

if promedio >= 6:
                 print(nombre + " felicidades has aprobado con un promedio de:", promedio)
                 #para controlar la cantidad de decimales que queremos, utilizamos "round"
                 print(nombre + " felicidades has aprobado con un promedio de:", round(promedio,2))
                 
else:
    print(nombre + " no has aprobado tu promedio es de:", promedio)
    print(nombre + " no has aprobado tu promedio es de:", round(promedio,1))
    

print("Fin.")


            
                 
