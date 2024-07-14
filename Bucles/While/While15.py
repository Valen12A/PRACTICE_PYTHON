numeros = []

while True:
    numero = int(input("Introduce cualquier número: "))
    if numero < 0:
        break
    numeros.append (numero)

print("Los números introducidos son:", numeros)
