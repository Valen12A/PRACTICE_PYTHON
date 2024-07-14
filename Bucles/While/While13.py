while True:
    contraseña = input("\nIngrese su contraseña: ")
    confirmarcontraseña = input("\nIngrese nuevamente su contraseña: ")
    if contraseña == confirmarcontraseña:
        print("\nLas contraseñas coinciden.")
        
        print ("\nAcceso concedido.")
        break
    else:
        print("\nLas contraseñas no coinciden.")
        print ("\nIntente de nuevo.")
