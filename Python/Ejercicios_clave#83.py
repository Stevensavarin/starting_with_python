print("Ejercicio #1")
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
num_manzanas = fruits.get("manzanas")
print(f"Cantidad de manzanas con el método get(): {num_manzanas}")
num_manzanas = fruits["manzanas"]
print(f"Cantidad de manzanas consultando el valor []: {num_manzanas}")

print("\nEjercicio #2")

fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
fruits["bananas"] = 5
print(f"Valor asignado: {fruits}")
fruits.setdefault("mangos", 6)
print(f"Método setdefault(): {fruits}")
fruits.update({"uvas": 3})
print(f"Método update(): {fruits}")

print("\nEjercicio #3")
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
del fruits["peras"]
print(f"Funcion del: {fruits}")
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
fruits.pop("peras")
print(f"Método pop(): {fruits}")

print("\nEjericio #4")

fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
keys_list = list(fruits.keys())
print(f"Lista de claves: {keys_list}")
values_list = list(fruits.values())
print(f"Lista de valores: {values_list}")

print("\nEjercicio #5")
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
print(f"La clave manzanas existe en el diccionario?:")
if "manzanas" in fruits:
    print(True)
else:
    print(False)



























