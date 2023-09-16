fruits_dict = {"manzana": 1.55,
               "banana": 3.55,
               "naranja": 1.25
               }

print(fruits_dict)

precio_manzana = fruits_dict.get("manzana")
print(f"El precio de la manzana es: {precio_manzana}")

precio_mango = fruits_dict.get("mango")
print(f"El precio del mango es: {precio_mango}")

precio_mango = fruits_dict.get("mango", 4.55)
print(f"El precio del mango es: {precio_mango}")
