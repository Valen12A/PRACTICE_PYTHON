import math 

def formulaCuadratica ():
    while True:
        try:
            a = int(input("\n Ingrese el primer numero: "))
            b = int(input("\n Ingrese el segundo numero: "))
            c = int(input("\n Ingrese el tercer numero: ")) 
            x1 = (b** b) - (4*a*c)
            x2 =-b + math.sqrt(x1)
            x3 = 2*a
            x4 = x2 / x3
        
            print ("\n La funcion cuadratica es: ",x4)
            
        except ValueError:
            print ("valor no valido")
            
        except ZeroDivisionError:
            print ("no se puede dividir por cero")
            
print(formulaCuadratica())