#EJERCICIO 7: VALIDAR CONTRASEÑA
password_correcto = "jeremi10"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    password_= input("Ingrese la contraseña: ")
    if password_== password_correcto:
        print("Acceso permitido.")
        break
    else:
        intentos += 1
        restantes = max_intentos - intentos
        if restantes > 0:
            print(f"Contraseña incorrecta. Te quedan {restantes} intentos. ")
        else:
            print("Demasiados intentos fallidos. Cuenta bloqueada. ")
