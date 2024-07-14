numero = int(input("Introduce un número: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print("\nEl factorial de", numero, "es", factorial)
