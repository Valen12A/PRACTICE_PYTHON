numero = int(input("Introduce un número entero mayor que cero: "))

print("Los divisores de", numero, "son:")

for total in range(1, numero+1):
    if numero % total == 0:
        print(total)
