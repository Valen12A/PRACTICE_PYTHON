numero1 = int(input("Ingrese el primer numero: "))

numero2 = int(input("Ingrese el segundo numero: "))

while numero1 > numero2:
    if numero1 >= numero2:
            numero1 -= numero2
    elif numero2 >= numero1:
            numero2 -=numero1
        
    else:
        if numero1 >= numero2:
            numero1 -= numero2
        else:
            numero2 >= numero1
            numero2 -= numero1
print("El resultado final de las restas posibles es: ", abs(numero1 - numero2))
