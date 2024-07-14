from Usuario import *
from Persona import *
from Estudios import *
from Empresa import *
from Buscar import *
from oferta import *
from ubicacion import *
from vacante import *

usuario = Usuario('Persona', 1234, 'pass1')
persona = Persona('Persona', 1234, 'pass1', '1 año', 'Ronald', 312, 'ronald@gmail', 'Cra77', 'Desempleado', 'Tecnico', '17-08-2005')
empresa = Empresa('001', 'Empresa@gmail', '10', 'Libre')
of1=Oferta(10001,'adidas',2,'12','12/03/2023','12/04/2023')

print(usuario.getDatos1())
print(persona.getDatos2())
print(empresa.getDatos3())
print(of1.getDatos6())
print()

print('1-Agragar Vacante')
print('2-Buscar Vacante')


while True:
    opcion = int(input('Elija la lista que desea usar: '))
    print()
    if opcion == 1:
        Vacante.almacenarVacante(Vacante.lista_cargos)
    elif opcion == 2:
        Buscar.buscarVacante()
    else:
        print('Ingrese una opcion valida')

Buscar.FiltrarOferta()
    
print()


                            

