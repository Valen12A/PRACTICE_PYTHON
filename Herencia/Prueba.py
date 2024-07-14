from Individual import *
from Empresa import *
from Producto import *

cliente1=Individual(1,'Individual','Camila Suarez','suarez1@gmail.com',3009258020)
cliente2=Empresa(1,'Empresa','ClasesConShreek',3026841004)
prod1=Producto(1,'Computador','Maquina Electronica',2049000, 3.5)
prod2=Producto(2,'Televisor','Aparato Electronico',1000000, 2)
cliente1.setProducto(prod1)
cliente1.setProducto(prod2)
print(cliente1.getTodo1())
print(cliente1.getTodo2())
print(cliente1.getTodo3())


#for producto in cliente1.getProducto():
#    print(producto.getNombre())
#print(ob.getTodo())