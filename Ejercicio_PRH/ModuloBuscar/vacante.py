class Vacante():
    lista_cargos=[]
    Van={}
    def __init__(self,id,ocupaciones,numVacante,salario,mesesExperiencia,tipoContrato,ubicacion,jornadaTrabajo):
        self.__id=id_vacante 
        self.__ocupaciones = ocupaciones
        self.__numVacante = numVacante
        self.__salario = salario
        self.__mesesExperiencia = mesesExperiencia
        self.__tipoContrato = tipoContrato
        self.__ubicacion = ubicacion
        self.__jornadaTrabajo = jornadaTrabajo
        Vacante.lista_cargos=[]
        Vacante.Van={}

    
    def almacenarVacante(lista_cargos):
        id_vacante = input("Ingrese el ID de la vacante: ")
        ocupaciones = input("Ingrese la ocupacion: ")
        numVacante = int(input("Ingrese el número de vacantes: "))
        salario = int(input("Ingrese el Salario: "))
        mesesExperiencia = int(input("Ingrese los Meses de experiencia requeridos: "))
        tipoContrato = input("Ingrese el Tipo de contrato: ")
        ubicacion = input("Ingrese la Ubicación: ")
        jornadaTrabajo = input("Ingrese el Tipo de jornada: ")
        
        Vacante.Van = {
        "id":id_vacante,
        "Ocupacion":ocupaciones,
        "Numero_vacantes":numVacante,
        "Salario":salario,
        "Meses de experiencia":mesesExperiencia,
        "Tipo de contrato":tipoContrato,
        "Ubicacion":ubicacion,
        "Tipo de jornada":jornadaTrabajo
        }
        Vacante.lista_cargos.append(Vacante.Van)
        print("Vacante almacenada correctamente.")
    

    print()
