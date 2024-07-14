def buscarArchivo(archivo):
    try:
        file = open(archivo, "r")
        linea=file.readlines()
        numLineas=len(linea)
        print(f"El archivo tiene {numLineas} lineas")
        file.close()

        archivo = open(archivo, "r")
        contenido = archivo.read()
        numCaracteres = len(contenido)
        archivo.close()
        print(f"El archivo contiene {numCaracteres} caracteres")

    except FileNotFoundError:
        print(f'El archivo {archivo} no existe.')

archivo = 'ActividadArchivos\\Archivo1.txt'
print(buscarArchivo(archivo))

def agregarArchivo (archivo):
    try: 
        with open(archivo, "a") as archivo:
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido:")
            numero = input("Ingrese su numero de celular: ")
            direccion = input("Ingrese su direccion: ")
            datos = [nombre, apellido, numero, direccion]
            for dato in datos:
                archivo.write (dato + "\n")
            print("Datos agregados con exito")
    except:
        print("Ha ocurrido un error")

archivo = 'ActividadArchivos\\tarea\\Archivo1.txt'
print(agregarArchivo(archivo))

archivo = 'ActividadArchivos\\tarea\\Archivo1.txt'
print(buscarArchivo(archivo))