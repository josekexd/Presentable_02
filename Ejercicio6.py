# EJERCICIO 6: PIRÁMIDE DE ASTERISCOS
N = int(input("Ingrese el número de filas de la pirámide: "))
for i in range(1, N + 1):
    # Espacios para centrar (opcional) - podrías imprimir sin espacios
    print(" " * (N - i) + "*" * (2 * i - 1))