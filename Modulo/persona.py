class persona:
    def __init__ (self, nombre, documento,):
        self.__nombre =nombre 
        self.__documento=documento
        self.__curso  = []
    
    def getNombre(self):
        return self.__nombre
    def setNombre (self, nombre):
        self.__nombre= nombre
    
    def getDocumento(self):
        return self.__documento
    def setDocumento (self, documento):
        self.__documento= documento

    
    
    
p= persona("ana", 123)
print(p.getNombre())

#q= persona ("pedro", 321)
#print(q.getNombre())

p= persona("ana", 123)
print(p.getDocumento())

#q= persona ("pedro", 321)
#print(q.getDocumento())





#p=persona ("ana", 123)
#print(p.setNombre())

#q=persona ("pedro", 321)
#print (q.setNombre())


#insertar
#consultra
#buscar
#eliminar  remove
#modificar