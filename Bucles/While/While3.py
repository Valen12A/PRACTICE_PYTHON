# imprimir una serie desde 1 hasta n (n ingresado por el usuario) 
#cada vez que encuentre un multiplo de 7 debe indicar 

n=int(input('ingrese numero: '))  #el usuario ingrasa un numero, el cula sera las veces que se repite el bucle 
i=1
while i<=n: # el siclo se repite hasta el numero ingresado por el usuario
    
    if i % 7 == 0:  #condicion en donde mostrara cuando un numero sea multiplo de 7
        
        print(f'{i} es multiplo de 7:')
        
    else: 
        
        print(i) 
    i+=1 # incrementara de uno en uno 