class empleado:
    prom = 0
    sumaSalarios = 0

    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        empleado.prom +=1
        empleado.sumaSalarios += self.__salario

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getCargo(self):
        return self.__cargo
    def setCargo(self,cargo):
        self.__cargo=cargo
    
    def salarioHora(self,horasTrabajadas):
        salario_hora=self.__salario / horasTrabajadas
        return salario_hora
    
    def incrementoSalario(self):
        if self.__salario > 1160000:
            ipc = self.__salario * 13.12 / 100
            incrementoSalario = self.__salario + ipc
            self.__salario = incrementoSalario
            return ipc
        else:
            ipc = self.__salario * 16.12 / 100
            incremento = self.__salario + ipc
            self.__salario = incremento
            return ipc
        
    def  horasExtras(self, horas): 
        if horas > 10:
            return f"Las horas extra ingresadas no coninciden."
        else:
            suma = 4833 * horas
            self.__salario = self.__salario + suma
            return f"las horas extra son correctas"

    def getSuma(self):
        return p.sumaSalarios
    
    def promedioSalarios(self):
        promSalarios = p.sumaSalarios / empleado.prom
        return promSalarios

    def getdatos(self):
         return f'{self.__nombre}, {self.__cargo},{self.__salario}'


p=empleado('Maria','Conductora',1500000)
print(p.getNombre())
print(p.getCargo())
horas_trab=int(input('Ingrese horas trabajadas: '))
salario_hora= p.salarioHora(horas_trab)
print(f'El empleado {p.getNombre()} gana {salario_hora:.2f} por hora')
print(f'El incremeto es de: {p.incrementoSalario()}')
print(p.horasExtras(2))
print(p.getdatos())


q=empleado('Juliana','Contadora',2500000)
print(q.getNombre())
print(q.getCargo())
horas_trab=int(input('Ingrese horas trabajadas: '))
salario_hora= q.salarioHora(horas_trab)
print(f'El empleado {q.getNombre()} gana {salario_hora:.2f} por hora')
print(f'El incremeto es de: {q.incrementoSalario()}')
print(q.horasExtras(6))
print(f'El promedio de los salarios es de: {q.promedioSalarios()}')
print(q.getdatos())


x=empleado('Juan','Secretario',1000000)
print(x.getNombre())
print(x.getCargo())
horas_trab=int(input('Ingrese horas trabajadas: '))
salario_hora= x.salarioHora(horas_trab)
print(f'El empleado {x.getNombre()} gana {salario_hora:.2f} por hora')
print(f'El incremeto es de: {x.incrementoSalario()}')
print(x.horasExtras(6))
print(f'La suma de los salarios es: {x.getSuma()}')
print(f'El promedio de los salarios es de: {x.promedioSalarios()}')
print(x.getdatos())
