# Acceder a los elementos de una tupla mediante el operador de segmentación

vowels_tuple = ("a", "e", "i", "o", "u")
print(vowels_tuple, "\n")

print(f"Posiciones [0:2] -> {vowels_tuple[0:2]}")
print(f"Posiciones [::2] -> {vowels_tuple[::2]}")
print(f"Posiciones [-3:] -> {vowels_tuple[-3:]}")
