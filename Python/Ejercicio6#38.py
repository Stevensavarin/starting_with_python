print("Ejercicio practico#6".center(50, "="))

string = input("Introduce una frase: "); string = string.lower() #test
palabra = input("Palabra que deseas eliminar: "); palabra = palabra.lower() #test
substring = ""
indice = string.find(palabra)
substring = string[0 : indice] + string[indice + len(palabra) + 1 : ]

print(f"Cadena con palabra eliminada: {substring.capitalize()}\n")


