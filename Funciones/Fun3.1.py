import random
l1=[]

tam=(random.randint(10,15))

def llenarLista(lista):
    lista=[]
    lista=[random.randrange(100,500) for i in range(tam)]
    return lista

def ascendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista



while True:
    numCuart=int(input("Ingrese el numero de cuartil a calcular(1 al 4)="))
    if numCuart <=3:  
        def calculaCuartil(lista):
            listaOrd = ascendente(lista[:]) 
            calcCuartil = int(numCuart * (len(listaOrd) + 1) / 4)
            return listaOrd[calcCuartil]
        break    
    else:
        print("Numero no valido") 

    
while True: 
    numQuint=int(input("Ingrese el numero de quintil a calcular(1 al 5)="))
    if numQuint <=4:
        def calculaQuintil(lista):
            listaOrd = ascendente(lista[:]) 
            calcQuint = int(numQuint * (len(listaOrd) + 1) / 5)
            return listaOrd[calcQuint]
        break
    else:
        print("Numero no valido") 


def crearCuartil(lista, cuartil):
        nuevoCuartil = lista[:cuartil]
        return nuevoCuartil

def crearQuintil(lista, quintil):
        nuevoQuintil = lista[:quintil]
        return nuevoQuintil


def sumaCuartil(lista, cuartil):
        sum=0
        for x in cuartil:
            sum+=x
        return sum
def promedioCuartil(lista, cuartil):
        return sumaCuartil(lista, cuartil)/len(cuartil)


def sumaQuintil(lista, quintil):
        sum=0
        for x in quintil:
            sum+=x
        return sum
def promedioQuintil(lista, quintil):
        return sumaQuintil(lista, quintil)/len(quintil)


l1 = llenarLista(l1)
print(l1)
print("El tamaño de la lista es:", tam)

print(ascendente(l1))

print("El cuartil que se solicito está en la posición:", calculaCuartil(l1))
cuartil = calculaCuartil(l1)
cuartil = crearCuartil(l1, cuartil)
print("El promedio de el cuartil solicitado es de:",promedioCuartil(l1, cuartil))

print("El quintil que se solicito está en la posición:", calculaQuintil(l1))
quintil= calculaQuintil(l1)
quintil = crearQuintil(l1, quintil)
print("El promedio de el quintil solicitado es de:",promedioQuintil(l1, quintil))