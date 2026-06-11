#EJERCICIO 2: TABLA DE MULTIPLICAR

numero = int(input("Ingresar numero"))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")