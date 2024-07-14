from Usuario import*
class Empresa(Usuario):
    def __init__(self,nit,email,numeroTrabajadores,tipoEmpresa):
        self.__nit=nit
        self.__email=email
        self.__numeroTrabajadores=numeroTrabajadores
        self.__tipoEmpresa=tipoEmpresa
    
    def getDatos3(self):
        return f'{self.__nit},{self.__email},{self.__numeroTrabajadores},{self.__tipoEmpresa}'

    def SubirOfreta():
        pass