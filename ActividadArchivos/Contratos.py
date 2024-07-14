class Contratos:
    def __init__(self,contrato,nit, fechaInicioContrato,fechaFinContrato):
        self.contrato = contrato
        self.nit = nit
        self.fechaInicioContrato = fechaInicioContrato
        self.fechaFinContrato = fechaFinContrato
        
        
        
    def datos (self):
        return f"{self.__contrato, self.__nit, self.__fechaInicioContrato, self.__fechaFinContrato}"
    
    def get1(self):
        return self.__nit
    
    def get3(self):
        return self.__contrato
    
    def get3(self):
        return self.__fechaInicioContrato
    
    def get4(self):
        return self.__fechaFinContrato


    