
numero = int(input("Ingrese un numero positivo: "))
n = int(input("Ingrese un numero para buscar multiplos: "))


cont = 0
for i in range(1, numero + 1):
    if i % n == 0:
        cont = + cont + 1


print (f"En la serie hay {cont} multipos de {n}")
