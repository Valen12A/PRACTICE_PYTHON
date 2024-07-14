def mayorLista(lista):        
    maximo = lista[0]                     
    for i in lista:
        if i > maximo:
            maximo=i
    return f"El numero mayor de la lista es: {maximo}"


def menorLista(lista):
    minimo=lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return f"El numero menor de la lista es: {minimo}"


def moda(lista):
    max=0
    for i in lista:
        cont=0
        for o in lista:
            if i == o:
                cont+=1
        if cont > max:
            max = cont
            moda1= i
    return f'La moda es: {moda1} ya que se repite {max}'


