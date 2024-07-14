# Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario indique al inicio del pro
import random 

def fibonacci(x):
    if x == 0:                      #Si x es igual a 0 devuelve una lista vacia.
        return 0
    elif x == 1:                    #Si x es igual a 1 devulve 0 ya que es el primer numero de la serie.
        return 1                    
    else:                           #Si no calcula la serie con la cantidaqd de dijitos que desea ver.
        num1 = 0
        num2 = 1

        for i in range(x - 1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3

        return num2

lista = []

num = int(input("Ingrese la cantidad de números de la serie de Fibonacci que desea ver: "))

for i in range(num):
    lista.append(random.randint(i))

print(lista)