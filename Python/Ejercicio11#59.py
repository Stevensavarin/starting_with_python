list1=["A", "B", "b", "c", "E", "E", "f"]
print(f"Lista original: {list1}")
element = input("Introduce el elemento a eliminar: ")
for _ in list1:
    if element.lower()in list1:
        list1.remove(element.lower())
    elif element.upper()in list1:
        list1.remove(element.upper())
print(f"lista final: {list1}\n")

