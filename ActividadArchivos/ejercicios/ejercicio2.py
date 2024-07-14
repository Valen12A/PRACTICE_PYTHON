try:
        with open("ActividadArchivos/himno.txt", "r", encoding= "utf-8") as file:
            cont = 1
            line = file.readline()
            for line in file:
                numCarcateres = len(line) 
                print(numCarcateres)
                print(f"{cont} {line}")
                cont +=1

        file.close()
except IOError as e:
    print(e)