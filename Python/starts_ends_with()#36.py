string = "Diana se peina sola"
resultado = 0
starts_with = "Ejemplo con startswith():"
ends_with = "Ejemplos con endswith():"

print(f"\n{starts_with.center(50, '=')}")

resultado = string.startswith("D")
print(f"\n{string} comienza con la subcadena D: {resultado}")

resultado = string.startswith("d")
print(f"\n{string} comienza con la subcadena d: {resultado}")

resultado = string.startswith("Diana")
print(f"\n{string} comienza con la subcadena D: {resultado}")

resultado = string.startswith("se", 6)
print(f"\n{string} comienza con la subcadena se, desde la posicion 6: {resultado}")

resultado = string.startswith("se", 6, 7)
print(f"\n{string} comienza con la subcadena se, desde la posicion 6 hasta la 7: {resultado}")

resultado = string.startswith("se", 100, 100)
print(f"\n{string} comienza con la subcadena se, desde la posicion 100 hasta la 100: {resultado}")

resultado = string.startswith("se", -4, -1)
print(f"\n{string} comienza con la subcadena se, desde la posicion -4 hasta la -1: {resultado}")


print(f"\n{ends_with.center(50, '=')}")

resultado = string.endswith("A")
print(f"\n{string} termina con la subcadena A: {resultado}")

resultado = string.endswith("a")
print(f"\n{string} termina con la subcadena a: {resultado}")

resultado = string.endswith("sola")
print(f"\n{string} termina con la subcadena sola: {resultado}")

resultado = string.endswith("sola", 10)
print(f"\n{string} termina con la subcadena sola, desde la posicion 10: {resultado}")

resultado = string.endswith("s", 9, 14)
print(f"\n{string} termina con la subcadena s, desde la posicion 9 hasta la 14: {resultado}")

resultado = string.endswith("s", 100, 100)
print(f"\n{string} termina con la subcadena s, desde la posicion 100 hasta la 100: {resultado}")

resultado = string.endswith("s", -4, -2)
print(f"\n{string} termina con la subcadena s, desde la posicion -4 hasta la -2: {resultado}")
