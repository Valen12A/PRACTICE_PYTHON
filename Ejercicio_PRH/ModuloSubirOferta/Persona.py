from Usuario import *

class Persona(Usuario):
    def __init__(self, tipoUsuario, numDocumento, contraseña, experienciaLaboral, nombre, telefono, email, direccion, situacionOcupacional, estudios, fechaNacimiento):
        super().__init__(tipoUsuario, numDocumento, contraseña)
        self.__experienciaLaboral = experienciaLaboral
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
        self.__direccion = direccion
        self.__situacionOcupacional = situacionOcupacional
        self.__estudios = estudios
        self.__fechaNacimiento = fechaNacimiento

    def subirHojaVida():
        pass

    def actualizarDatos():
        pass

    def buscarOfertas():
        pass

    def incribirOfertas():
        pass

    def restablecerContraseña():
        pass