numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
if numero1 > numero2 and numero1 > numero3:
    print("El primer número es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print("El segundo número es el mayor")
elif numero3 > numero1 and numero3 > numero2:
    print("El tercer número es el mayor")
else:
    print("Hay números iguales")
