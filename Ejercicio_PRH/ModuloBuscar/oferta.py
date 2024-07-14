class Oferta:
    def __init__(self,codigo,empresa,puesto,numPostulaciones,fechaInicio,fechaCierre):
        self.__codigo=codigo
        self.__empresa = empresa
        self.__puesto = puesto
        self.__numPostulaciones = numPostulaciones
        self.__fechaInicio = fechaInicio
        self.__fechaCierre = fechaCierre
    
    def getCodigo(self):
        return self.__codigo
        def setCodigo(self,codigo):
            self.__codigo=id

    def getEmpresa(self):
        return self.__empresa
    def setEmpresa(self,empresa):
        self.__empresa=empresa
    
    def getVacantes(self):
        return self.__vacante
    def setVacantes(self,vacante):
        self.__vacante=vacante
    
    def getNumPostulados(self):
        return self.__numPostulaciones
    def setNumPostulados(self,numPostulaciones):
        self.__numPostulaciones=numPostulaciones
    
    def getFchaInicio(self):
        return self.__fechaInicio
    def setFechaInicio(self,fechaInicio):
        self.__fechaInicio=fechaInicio
    
    def getFechaCierre(self):
        return self.__fechaCierre
    def setFechaCierre(self,fechaCierre):
        self.__fechaCierre=fechaCierre
    
    def getDatos6(self):
        return f'{self.__codigo},{self.__empresa},{self.__puesto},{self.__numPostulaciones},{self.__fechaInicio},{self.__fechaCierre}'
    
    def filtrarOferta():
        pass