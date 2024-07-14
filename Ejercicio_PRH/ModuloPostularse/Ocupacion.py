from Vacante import *

class Ocupacion(Vacante):
    def __init__(self, codigo, nombreCargo, funciones, descripcion, grupoPrimario):
        self.__codigo = codigo
        self.__nombreCargo = nombreCargo
        self.__funciones = funciones
        self.__descripcion = descripcion
        self.__grupoPrimario = grupoPrimario