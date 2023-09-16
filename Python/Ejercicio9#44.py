frase = input ("Introduce una frase: ")
letra = input ("Con que letra deseas finalizar el bucle?: ")

for x in frase:
    if x.lower() == letra.lower():
        break

    elif x.lower()== "a":
        continue

    elif x.lower()== "e":
        continue

    elif x.lower()== "i":
        continue

    elif x.lower()== "o":
        continue

    elif x.lower()== "u":
        continue
    print(x, end="")

print()

#Ejemplo 2

frase2 = input("Introduce una frase: ")
termino = input("Con que letra deseas finalizar el bucle?: ")
var = ""
var2 = ""

for i in frase2:
    if i == termino.lower() or i == termino.upper():
        break
    elif i != termino:
        var = i.strip("aeiouáéíóúAEIOUÁÉÍÓÚ")
        var2 = var2 + var
    else:
       print("Error inesperado")

print(var2)

