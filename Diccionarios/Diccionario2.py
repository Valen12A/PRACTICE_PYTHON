d1 = {"pollo": "chicken", "pato": "duck", "perro": "dog","tortuga": "tortoise"}

def ani1(d1):
    l1=[]
    l2=[]
    for clave,valor in d1.items():
        l1.append({clave})
        l2.append({valor})
        tuplaEs = tuple(l1)
        tuplaIn = tuple(l2)
    return (tuplaEs, tuplaIn)
  
tupla1, tupla2= ani1(d1)
print ("La tupla en español es: ", tupla1)
print ("La tupla y con los significados es: ", tupla2)