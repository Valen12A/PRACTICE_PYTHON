from Cliente import *

class Individual(Cliente):

    def __init__(self,identificador, tipo, nombre, correo, telefono):
        super().__init__(identificador, tipo)
        self.__nombre=nombre
        self.__correo=correo
        self.__telefono=telefono
        self.__producto=[]

    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre

    def setCorreo(self, correo):
        self.__correo=correo

    def getCorreo(self):
        return self.__correo

    def setTelefono(self, telefono):
        self.__telefono=telefono

    def getTelefono(self):
        return self.__telefono

    def setProducto(self,producto):
        self.__producto.append(producto)

    def getProducto(self):
        return self.__producto
    
    def getTodo1(self):
        return print(f'{self.__identificador},{self.__tipo},{self.__nombre}, {self.__correo}, {self.__telefono}, {self.__producto}')

