string = input("Introduce la frase o palabra que deseas invertir: ")
string_reversed = ""

for character in string:
    string_reversed = character + string_reversed
print(f"El string invertido: {string_reversed}")

