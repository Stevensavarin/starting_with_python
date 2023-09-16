dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }

print(dictionary)
print(f"\nLas keys del diccionario son:\n{dictionary.keys()}")

print("\nConvirtiendo keys a la lista utilizando el constructor keys")
list_keys = list(dictionary.keys())

print(f"La lista es: {list_keys}")
print(f"Posicion 1 de la lista keys: {list_keys[1]}")
