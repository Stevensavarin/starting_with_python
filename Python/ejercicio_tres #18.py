print("**********************************************************************")
print("* Programa para determinar cual es el numero mas grande de 3 numeros *")
print("********************************************************************** \n")

numero = int(input("Introduce el primer numero:"))
numeroo = int(input("Introduce el segundo numero:"))
numerooo = int(input("Introduce el tercer numero:"))

if numero > numeroo and numero > numerooo:
    print("El primer numero (",numero,") es el numero mayor")
elif numeroo > numero and numeroo > numerooo:
    print("El segundo numero (",numeroo,") es el numero mayor")
elif numerooo > numero and numerooo > numeroo:
    print("El tercer numero (",numerooo,") es el numero mayor")

print("...fin...")
