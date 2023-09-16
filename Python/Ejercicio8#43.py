numero = int(input("Que tabla de multiplicar quieres ver: "))
tabla = 0
print(f"La tabla del {numero} es:")
for x in range (0, 11, 1):
    tabla = (numero * x)
    print(f"{numero} x {x} = {tabla}")

#Ejemplo2

a = int(input("Que tabla de multiplicar quieres ver: "))
print(f"La tabla del {a} es:")
for i in range (11):
    print(f"{a} x {i} = {a*i}")
         
