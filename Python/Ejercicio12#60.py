lista = [1, 2, 3, 4, 5]
list1 = [1, 2, 3, 4, 5]
eliminado = [lista.pop(0),lista.pop()]

print(f"Lista original: {list1} \nLista resultante: {lista} \nNumeros eliminados: {eliminado}")

#Ejemplo 2
numeros = [1, 2 , 3, 4, 5]
print(f"\nLista números: {numeros}")
numeros_eliminados = []
numeros_eliminados.append(numeros.pop(0))
numeros_eliminados.append(numeros.pop())
print(f"Lista números: {numeros} \nLista números eliminados: {numeros_eliminados}")


