#declaracion de variables
num1,num2 =3,5


while  not (num1 % num2 ==0 or num2 % num1==0):  # verifica si los dos numero ingresados son factores
    
    
    num1 = int(input("Ingrese el primer numero: ")) #el usuario ingresa el primer numero 
    
    num2 = int(input("Ingrese el segundo numero: ")) #el usuario ingresa el segundo numero 
    
print (f"{num1} y {num2} son factores")            #inprime si los dos numeros son factores 
    
    
    


