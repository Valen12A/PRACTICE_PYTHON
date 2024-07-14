num=1
cont=0
sum = 0                  # definicion de variables
menor = 1000000
mayor = 0


while num!=0:  # el numero ingresado puede ser cualquiera
            # si ingresa 0 finaliza el programa 
            
    num=int(input('ingrese un numero:'))  #el usuario ingresa numeros hasta que digite 0
    
    cont=cont+1                           #el contador es una variable que es igual a la misma variable mas una contante.

    sum=sum+num
    
    if num>mayor:                         #condicion que identifica cual es el numero mayor de los ingresados
        mayor=num
        
    if num<menor and num!=0:              #condicion que identifica cual es el numero menor de los ingresados
        menor=num
    
 
print(f'fueron ingresados {cont-1} numeros')
print ("La suma de los numeros es:", sum )
print(f'El promedio es {sum/(cont-1)}')
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')
