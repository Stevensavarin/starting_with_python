print("*************************************")
print("* Calculadora con una sola variable *")
print("************************************* \n")

print("********************")
print("* Menu de opciones *")
print("********************")
print("""1)Suma
2)Resta
3)Multiplicacion
4)Division
5)Division entera
6)Exponente
7)Modulo o resto\n""")

a = int(input("Introduce la opcion deseada:"))

if a == 1:
    print("Elegiste suma \n")
    a = int(input("Introduce el primer numero:"))
    a += int(input("Introduce el segundo numero:"))
    a = print("El resultado de la suma es:",a )
elif a == 2:
    print("Elegiste resta \n")
    a = int(input("Introduce el primer numero:"))
    a -= int(input("Introduce el segundo numero:"))
    a = print("El resultado de la resta es:",a )
elif a == 3:
    print("Elegiste multiplicacion \n")
    a = int(input("Introduce el primer numero:"))
    a *= int(input("Introduce el segundo numero:"))
    a = print("El resultado de la multiplicacion es:",a )
elif a == 4:
    print("Elegiste division \n")
    a = int(input("Introduce el primer numero:"))
    a /= int(input("Introduce el segundo numero:"))
    a = print("El resultado de la division es:",round (a, 2))
elif a == 5:
    print("Elegiste division entera \n")
    a = int(input("Introduce el primer numero:"))
    a //= int(input("Introduce el segundo numero:"))
    a = print("El resultado de la division entera es:",a )
elif a == 6:
    print("Elegiste exponente \n")
    a = int(input("Introduce el primer numero:"))
    a **= int(input("Introduce el segundo numero:"))
    a = print("El resultado del exponente es:",a )
elif a == 7:
    print("Elegiste modulo o resto \n")
    a = int(input("Introduce el primer numero:"))
    a /= int(input("Introduce el segundo numero:"))
    a = print("El resultado del modulo o resto es:",a )
else:
    print("\nEsta opcion no es correcta \n")
print("...Fin..")        


    
    
