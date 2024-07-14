while True:
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    
    if numero1 < numero2 or numero2 < numero1:
        print ("fin del siclo")
        break
    else:
        print("Nuevo intento")
