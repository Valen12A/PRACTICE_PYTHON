p = int(input("Valor inicial: "))
s = int(input("Valor final : "))
t = int(input("Cantidad a incrementar: "))

for i in range(int((s - p) / t) + 1):
    
    print(p + i * t)
