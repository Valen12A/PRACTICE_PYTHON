from vacante import *
class Buscar(Vacante):
    def __init__( self,id,ocupacion,numVacante,salario,mesesExperiencia,tipoContrato,ubicacion,jornadaTrabajo,cargo,experiencia,rangoSalarial):
        Vacante().__init.__(id,ocupacion,numVacante,salario,mesesExperiencia,tipoContrato,ubicacion,jornadaTrabajo)
    
    def buscarVacante():
        for Vacante.Van in Vacante.lista_cargos:
            id_busqueda=input('Ingrese el id de la vacante a buscar: ')
            if Vacante.Van["id"] == id_busqueda:
                print("Vacante encontrada:")
                print("ID: ", Vacante.Van["id"])
                print("Ocupación: ", Vacante.Van["Ocupacion"])
                print("Número de vacante: ", Vacante.Van["Numero_vacantes"])
                print("Salario: ", Vacante.Van["Salario"])
                print("Meses de experiencia requeridos: ", Vacante.Van["Meses de experiencia"])
                print("Tipo de contrato: ", Vacante.Van["Tipo de contrato"])
                print("Ubicacion: ", Vacante.Van["Ubicacion"])
                print("Tipo de jornada: ", Vacante.Van["Tipo de jornada"])
            else:
                print("Vacante no encontrada.")

    def FiltrarOferta():
        pass