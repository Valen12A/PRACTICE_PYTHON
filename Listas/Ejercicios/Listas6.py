import random
lista1=[]
suma1=0
mayor1=0
menor1=0
lista2=[]
suma2=0
mayor2=0
menor2=0
tam1=0
tam2=0
promedio1=0
promedio2=0


tam1= random.randint(5,10)

for i in range(tam1):
    num=random.randrange(10)
    lista1.append(num)
print(lista1)


tam2= random.randint(5,10)

for i in range(tam2):
    num=random.randrange(10)
    lista2.append(num)
print(lista2)

#SUMA 
for i in lista1:
    suma1 += i 
print(suma1)


for i in lista2:
    suma2 += i 
print(suma2)

if suma1 > suma2:
    print (f'La suma de la lista 1 es {suma1} y es mayor que la suma de la lista 2: {suma2}')
else:
    suma1 > suma2
    print (f'La suma de la lista 2 es {suma2} y es mayor que la suma de la lista 1: {suma1}')

# MAYOR Y MENOR 

for i in lista1:
        if i>mayor1:
             mayor1=i
        if i<menor1:
             menor1=i
print("El mayor de la lista 1 es: ", mayor1)
print("El menor de la lista 1 es: ", menor1)



for i in lista2:
        if i>mayor2:
             mayor2=i
        if i<menor2:
             menor2=i
print("El mayor de la lista 2 es: ", mayor2)
print("El menor de la lista 2 es: ", menor2)



if mayor1 > mayor2:
    print (f'El numero mayor de la lista 1: {mayor1} es mayor que el de la lista 2: {mayor2}')
else:
    mayor2 > mayor1
    print (f'El numero mayor de la lista 1: {mayor2} es mayor que el de la lista 2: {mayor1}')


 
if menor2 > menor1:
    print (f'El numero menor de la lista 1: {menor1} es menor que el de la lista 2: {menor2}')
else:
    menor1 > menor2
    print (f'El numero menor de la lista 2: {menor2} es menor que el de la lista 1: {menor1}')

#PROMEDIO DE LAS DOS LISTAS SUMADAS 

promedio_conjunto=(suma1+suma2)/(tam1+tam2)
print("El promedio de las dos listas sumadas es: ", promedio_conjunto)



promedio1= suma1/tam1
print ("El promedio de la lista 1 es:", promedio1)

if promedio1 > promedio_conjunto:
    print (f'El promedio de la lista 1: {promedio1} es mayor que el promedio conjunto: {promedio_conjunto}')
else:
    promedio_conjunto > promedio1
    print (f'El promedio conjunto: {promedio_conjunto} es mayor que el promedio de la lista 1: {promedio1}')



promedio2= suma2/tam2
print ("El promedio de la lista 2 es:", promedio2)

if promedio2 > promedio_conjunto:
    print (f'El promedio de la lista 2: {promedio2} es mayor que el promedio conjunto: {promedio_conjunto}')
else:
    promedio_conjunto > promedio2
    print (f'El promedio conjunto: {promedio_conjunto} es mayor que el promedio de la lista 2: {promedio2}')


pares1=0
pares2=0
impares1=0
impares2=0

# CUAL DE LOS DOS TIENE MAYOR CANTIDAD DE PARES E IMPARES

for i in lista1:
     if i % 2 == 0:
          pares1+=1
print("La lista 1 tiene", pares1, "Numeros pares")
for i in lista2:
     if i % 2 == 0:
          pares2+=1
print("La lista 2 tiene", pares2, "Numeros pares")



for i in lista1:
     if i % 2 == 2:
          impares1+=1
print("La lista 1 tiene", impares1, "Numeros impares")
for i in lista2:
     if i % 2 == 1:
          impares2+=1
print("La lista 2 tiene", impares2, "Numeros impares")