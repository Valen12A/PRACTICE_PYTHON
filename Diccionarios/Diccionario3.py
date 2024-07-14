
dic1={}
dic2={}

def agregar_d1(l1, clave, valor, diccionario):
    lis=0
    diccionario.update({clave:valor})
    while True:
        lis +=1
        clave = input('Ingrese la clave: ')
        valor= input('Ingrese un valor: ')
        diccionario.update({clave:valor})
        if lis == l1:
            break          
    return True

def agregar_d2(l2, clave, valor, diccionario):
    diccionario.update({clave:valor})

    for i in range(1, l2):
        clave = input('Ingrese la clave: ')
        valor= input('Ingrese un valor: ')
        diccionario.update({clave:valor})
    return True

def actualizar(diccionario):
    print()
    print('Diccionario:')
    for m1 in diccionario:
        claves = diccionario[m1]
        print(f"{m1} = {claves}") 

print('Elija el diccionarios que desea llenar: ')
print('1 o 2')

pregunta= int(input('Escriba la opcion que desea: '))

match pregunta:
    case 1:
        print('Debe escribir la palabra en español y su respectivo significado en ingles')
        agregar_d1(int(input('Cuantas veces quiere llenar el diccionario: ')), input('Escriba la clave: '), input('Escriba el valor: '),dic1)
        actualizar(dic1)
    case 2:
        print('Debe escribir la palabra en ingles y si respectivo significado en español')
        agregar_d2(int(input('Cuantas veces quiere llenar el diccionario: ')), input('Escriba la clave: '), input("Escriba el valor: "),dic2)
        actualizar(dic2)  