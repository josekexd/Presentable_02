# EJERCICIO 4: MENÚ DE OPCIONES (SIMULANDO DO-WHILE)
while True:
    print("\n--- MENÚ ---")
    print("1. Opcion A")
    print("2. Opcion B")
    print("3. Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        print("Realizando opcion A....")
    elif opcion == "2":
        print("Realizando opcion B....")
    elif opcion == "3":
        print("Saliendo.")
        break
    else:
        print("Opcion inválida, intenta de nuevo. ")