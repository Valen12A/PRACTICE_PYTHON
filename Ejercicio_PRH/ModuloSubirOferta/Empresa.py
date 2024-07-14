from Usuario import *

class Empresa(Usuario):
    def __init__(self,nit,email,numeroTrabajadores,tipoEmpresa):
        self.__nit = nit
        self.__email = email
        self.__numeroTrabajadores = numeroTrabajadores
        self.__tipoEmpresa = tipoEmpresa
        self.__oferta = []

    def SubirOfreta():
        pass