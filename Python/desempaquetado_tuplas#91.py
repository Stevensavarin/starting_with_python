fruits_tuple = ("001", "Manzana", "rojo"), ("002", "Pera", "verde"), ("003", "Naranja", "naranja")
print(fruits_tuple, "\n")

for code, fruit, color in fruits_tuple:
    print(f"La {fruit} tiene el código {code} y es de color {color}.")
