class Producto:
    rebaja=0
    def __init__(self, identificador, nombre, tipo, precio, descuento):
        self.__identificador=identificador
        self.__nombre=nombre
        self.__tipo=tipo
        self.__precio=precio
        self.__descuento=descuento
        Producto.rebaja


    def setIdentificador(self, identificador):
        self.__identificador=identificador

    def getIdentificador(self):
        return self.__identificador

    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre

    def setTipo(self, tipo):
        self.__tipo=tipo

    def getTipo(self):
        return self.__tipo

    def setPrecio(self,precio):
        self.__precio(precio)

    def getPrecio(self):
        return self.__precio
    
    def setDescuento(self, descuento):
        self.__descuento(descuento)
    
    def getDescuento(self):
        return  self.__descuento
    
    def setDescuento(self,descuento):
        self.__descuento=descuento
    
    def Rebaja(self):
        rebaja=self.__precio * self.__descuento // 100
        return rebaja
    
    def getTodo3(self):
        return f'{self.__identificador},{self.__nombre},{self.__tipo},{self.__precio},{self.__descuento}'