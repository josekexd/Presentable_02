# EJERCICIO 10: JUEGO DE ADIVINAR
import random

secreto = random.randint(1, 100)
intentos_realizados = 0
max_intentos = 10
puntaje_inicial = 100
adivinado = False

print("Adivina el número secreto (entre 1 y 100)")

while intentos_realizados < max_intentos and not adivinado:
    try:
        guess = int(input(f"Intento {intentos_realizados + 1}: "))
    except ValueError:
        print("Error: ingresa un número válido")
        continue

    intentos_realizados += 1

    if guess == secreto:
        adivinado = True
        # Puntaje: se resta 10 por cada intento fallido (solo los usados)
        puntaje_final = puntaje_inicial - (intentos_realizados - 1) * 10
        print(f"¡Felicidades! Adivinaste en {intentos_realizados} intentos.")
        print(f"Tu puntaje es: {puntaje_final}")
    elif guess < secreto:
        print("Pista: el número es MAYOR")
    else:
        print("Pista: el número es MENOR")

if not adivinado:
    print(f"Agotaste tus {max_intentos} intentos. El número era {secreto}. Puntaje: 0")