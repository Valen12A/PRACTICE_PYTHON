def div ():
    while True:
        try: 
            n1 = int(input("Ingrese el primer numero: "))
            n2 = int(input("Ingrese el segundo numero: "))
            if n1 / n2 or n2 / n1:
                producto = n1 / n2
                print (f"La divicion de {n1} entre {n2} es: {producto}")
        
        except ZeroDivisionError:
            print ("No se puede dividir por cero")
        except ValueError:
            print ("Valor no valido :( ")
        except:
            print ("No fue posible")
        print ("FIN")
    