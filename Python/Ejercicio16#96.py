names_tuple = ("Ana", "Gerardo", "Maria", "Carlos", "Valentina")
print(names_tuple, "\n")

validator = 0
while validator ==0:
    number = int(input("Introduce un numero entre 0 y 4: "))

    if 0 <= number <= 4:
        print(f"El nombre es: {names_tuple[number]}")
        validator = 1
    else:
        print("¡Error!: Número invalido vuelve a intentar. \n")
