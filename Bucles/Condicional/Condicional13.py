numero1= int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

if numero1 > numero2:
    numero_mayor = numero1
    numero_menor = numero2
else:
    numero_mayor = numero2
    numero_menor = numero1

if numero_mayor % numero_menor == 0:
    print("El número mayor es múltiplo del menor.")
else:
    print("El número mayor no es múltiplo del menor.")
