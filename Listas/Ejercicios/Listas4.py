#suma, promedio, minimo, maximo, moda, media, desviasion estandar.
import random
lista = []
suma = 0
menor= 0
mayor = 0
prom = 0

tam = random.randint(10, 20)
print (tam)
for i in range (tam):
    num=random.randrange(100)
    lista.append(num)  
print (lista)

for  i in lista:
    suma = + suma + i
print ("la suma es: ", suma)


for i in range (len(lista)):
    suma += lista[i]
    prom = suma// len (lista)
print ("el promedio es: ", prom)

for i in lista:
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i
print ("el numero mayor es: ", mayor)
print ("el numero menor es:", menor)


        