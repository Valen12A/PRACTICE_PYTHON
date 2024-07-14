from Contratos import *
from operaciones import *
import csv

contratos = []



with open("ActividadArchivos\Contratos_de_concesi_n_de_juegos_de_suerte_y_azar.csv", "r", newline="") as Archivo:
    lee = csv.reader(Archivo)
    for row in lee:
        objeto = Contratos(row[0], row[1], row[3], row[4])
        contratos.append(objeto)



with open("ActividadArchivos/contrato1.txt", "w", newline='')as file:
    contrato1 = csv.writer(file)
    contrato1.writerow(["contrato", "nit", "fechaInicioContrato", "fechaFinContrato"])
    
    # m =('La moda es: ', moda(contrato1))
    # my =('El mayor es: ', mayorLista(contrato1))
    # mn =('El menor es: ', (contrato1))

    for contrato in contratos:
        contrato1.writerow([contrato.contrato, contrato.nit, contrato.fechaInicioContrato, contrato.fechaFinContrato])
    # for contrato in contratos:
    #     contrato1.writerow([m, my, mn])

