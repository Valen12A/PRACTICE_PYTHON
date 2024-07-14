import random 
#llenar lista.

def llenarlista(tam,rango):
    lista1=[]
    lista1=[random.randrange(rango) for i in range(tam)]
    return lista1

def llenarlista(tam,rango):
    lista2=[]
    lista2=[random.randrange(rango) for i in range(tam)]
    return lista2

#calcular suma.

def sumalista(lista1):
    sum1=0
    for x in lista1:
        sum1+=x
    return sum1

    
def sumalista(lista2):
    sum2= 0
    for x in lista2:
        sum2+=x
    return sum2


def sumaMayor(lista1, lista2):
    sum1 = sum (lista1)
    sum2 = sum (lista2)

    if sum1 > sum2:
        return f"el numero mayor de la suma es de la lista1  {sum1}. "
    elif sum1 < sum2:
        return f"el numero mayor de la suma es de la lista2 {sum2} "
    else:
        return " las dos listas tienen la misma suma. "

#Calcular mayor.

def mayorlista(lista1):
    maximo=lista1[0]
    for i in lista1:
        if i>maximo:
            maximo=i
    return maximo

def mayorlista(lista2):
    maximo=lista2[0]
    for i in lista2:
        if i>maximo:
            maximo=i
    return maximo


def mayordoslistas(lista1, lista2):
    num1 =  max (lista1)
    num2 =  max (lista2)

    if num1 > num2:
        return f" el numero mayor es de {num1} de la lista 1"
    elif  num1 < num2:
        return f" {num2} de la lista 2 "
    else:
        return f" tienen el mismo numero"

#Calcular menor.

def menorlista(lista1):
    minimo=lista1[0]
    for i in lista1:
        if i<minimo:
            minimo=i
    return minimo

def menorlista(lista2):
    minimo=lista2[0]
    for i in lista2:
        if i<minimo:
            minimo=i
    return minimo


def menordoslistas(lista1, lista2):
    num1 =  min (lista1)
    num2 =  min (lista2)

    if num1 < num2:
        return f" el numero ,menor es de {num1} de la lista 1"
    elif  num1 > num2:
        return f" {num2} de la lista 2 "
    else:
        return f" tienen el mismo numero"

#promedio
def promediolista(lista1):
    return sumalista(lista1)/len(lista1)


def promediolista(lista2):
    return sumalista(lista2)/len(lista2)


lista1 = llenarlista (5, 10)
lista2 = llenarlista (5, 10)
print (lista1)
print (lista2)
print (f"Suma lista 1: ", sumalista (lista1))
print (f"Suma lista 2: ", sumalista (lista2))
print ("", sumaMayor (lista1, lista2))
print ("El mayor de la lista1 es : ", mayorlista(lista1) )
print ("El mayor de la lista2 es : ", mayorlista(lista2) )
print (f"El numero mayor es {mayordoslistas (lista1, lista2)}" )
print ("El menor de la lista1 es : ", menorlista(lista1) )
print ("El menor de la lista2 es : ", menorlista(lista2) )
print (f"El numero menor es {menordoslistas (lista1, lista2)}" )