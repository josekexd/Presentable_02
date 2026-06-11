# EJERCICIO 9: FIBONACCI HASTA N
N = int(input("Ingrese el límite N para la serie de Fibonacci: "))
a, b = 0, 1
print("Números de Fibonacci menores que", N, ":")
if N > 0:
    print(a, end=" ")
while b < N:
    print(b, end=" ")
    a, b = b, a + b
print() 