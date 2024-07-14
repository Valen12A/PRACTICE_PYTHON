import random
lista=[]
posiciones_numero_buscar=[]
contador=0
tam= random.randint(15,20)

for i in range(tam):
    num=random.randrange(0,9)
    lista.append(num)

numero_buscar= int(input("Ingrese el numero que desea buscar:"))

while numero_buscar not in  lista:
        print("El numero no en la lista.")
        numero_buscar= int(input("Ingrese el numero que desea buscar:"))

for i in lista:
    if i == numero_buscar:
        contador+=1

print(f"El numero {numero_buscar} en la lista {lista} aparece {contador} veces")

for i in range(len(lista)): 
   if numero_buscar == lista [i]:
        print(f'{lista[i]} esta en la posicion {i}')