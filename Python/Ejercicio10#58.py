i = int(input("Cuantos numeros quieres que tenga la lista?: "))
lista = []
bucle = 0

while bucle < i:
    lista.append(int(input('Ingresa un numero entero: ')))
    bucle += 1

print(f"Lista: {lista}")
print(f"La suma total de los elementos es: {sum(lista)}")

#Ejemplo 2
numeros = []
longitud_lista = int(input("\nCuantos números quieres que tenga la lista?: "))

for e in range(longitud_lista):
    numeros.append(int(input("Introduce un número entero: ")))

print(f"\nLista: {numeros} \nLa suma total de los elementos es: {sum(numeros)}")


      
    
