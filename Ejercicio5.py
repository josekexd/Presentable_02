# EJERCICIO 5: NUMERO PRIMOS 
numero = int(input("Ingrese un número entero positivo: "))
if numero <= 1:
    print("No es primo (debe ser mayor que 1)")
else:
    es_primo = True
    # Solo necesitamos divisores hasta la raíz cuadrada
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")