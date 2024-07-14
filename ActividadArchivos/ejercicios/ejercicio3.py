try:
        file = open("ActividadArchivos/himno.txt", "r", encoding= "utf-8")
        #print (file.readlines())
        
        for line in file.readlines():
            print (line)
            
except IOError as e:
    print (e)
    
