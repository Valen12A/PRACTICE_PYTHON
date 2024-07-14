import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='proyecto_sena'
)

cursor = database.cursor()

def insertar_empresa():
    nit = input('Ingrese el nit de la empresa: ')
    nombre = input('Ingrese el nombre de la empresa: ').upper()
    email = input('Ingrese el correo: ').lower()
    telefono = input('Ingrese el numero de telefono: ')
    direccion = input('Ingrese la direccion: ').lower()
    tipoEmpresa = input('Ingrese el tipo de empresa (PUBLICA, PRIVADA, MIXTA): ')
    numTrabajadores = input('Ingrese el numero de trabajadores: ')

    consulta = 'INSERT INTO empresa (nit, nombre, email, telefono, direccion, tipoEmpresa, numTrabajadores) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    valores = (nit, nombre, email, telefono, direccion, tipoEmpresa, numTrabajadores)

    cursor.execute(consulta, valores)
    database.commit()

    print('Empresa creada con exito.')

insertar_empresa()



