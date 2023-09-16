print("Asignacion:")
mensaje ="Hola" 
mensaje +=" "
mensaje +="Steven"
print(mensaje)
print(" ")

print("Concatenacion:")
mensaje ="Hola"
espacio =" "
nombre ="Steven"
print(mensaje + espacio + nombre)
print(" ")

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)
print(" ")

print("Busqueda:")
mensaje = "Hola Steven"
buscar_subcadena = mensaje.find("Steven")
print(buscar_subcadena)
print(" ")

print("Extraccion:")
mensaje = "Hola Steven"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)
print(" ")
    
print("Comparacion:")
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)
print(" ")
mensaje_uno = "Hola"
mensaje_dos = "Steven"
print(mensaje_uno == mensaje_dos)


