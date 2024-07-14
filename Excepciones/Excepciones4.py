dic={'ciudad':'Soacha',
    'continente':'Africa',
    'planeta':'Marte',
    'pais':'España'}

def clave(key, diccionario):
    if key  in diccionario:
        
        if key in diccionario:
            l1= diccionario [key]

    else: 
        return f"La clave {key} no esta en el diccionario"
print(clave(input("Escriba la clave a buscar: "), dic))