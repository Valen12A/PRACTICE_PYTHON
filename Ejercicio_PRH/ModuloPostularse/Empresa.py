from Usuario import *

class Empresa(Usuario):
    def __init__(self,nit,email,numTrabajadores,tipoEmpresa):
        Usuario.__init__()
        self.__nit = nit
        self.__email = email
        self.__numTrabajadores = numTrabajadores
        self.__tipoEmpresa = tipoEmpresa
        self.__oferta = []



    def SubirOfreta():
        pass

    def mostrar_empresa(self ):
        return f'{self.__nit},{self.__email}, {self.__numTrabajadores}, {self.__tipoEmpresa}, {self.__oferta}' 