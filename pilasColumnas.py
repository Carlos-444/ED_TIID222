while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Colas")
    print("2. Pilas")
    print("3. Salir")
    
    opcion_principal = input("Seleccione una opción (1-3): ")

    if opcion_principal == "1":
        cola = []
        while True:
            print("\n--- MENÚ DE COLAS ---")
            print("1. Insertar cola")
            print("2. Borrar en cola")
            print("3. Listar cola")
            print("4. Regresar al menú principal")
            
            opcion = input("Seleccione una opción (1-4): ")

            if opcion == "1":
                numero = int(input("Ingrese el número a insertar en la cola: "))
                cola.append(numero)
                print(f"Número {numero} ingresado con éxito.")

            elif opcion == "2":
                if len(cola) > 0:
                    eliminado = cola.pop(0)
                    print(f"Se borró el elemento: {eliminado}")
                else:
                    print("La cola está vacía")

            elif opcion == "3":
                if len(cola) > 0:
                    print("Elementos en la cola (Frente-----Final):", cola)
                else:
                    print("La cola está actualmente vacía.")

            elif opcion == "4":
                break

            else:
                print("Opción no válida.")
                
                
                #Pilas

    elif opcion_principal == "2":
        pila = []
        while True:
            print("\n--- MENÚ DE PILAS ---")
            print("1. Insertar en pila")
            print("2. Borrar en pila")
            print("3. Listar pila")
            print("4. Regresar al menú principal")
            
            opcion = input("Seleccione una opción (1-4): ")

            if opcion == "1":
                numero = int(input("Ingrese el número a insertar en la pila: "))
                pila.append(numero)
                print(f"Número {numero} apilado con éxito.")

            elif opcion == "2":
                if len(pila) > 0:
                    eliminado = pila.pop()
                    print(f"Se quitó el elemento de la cima: {eliminado}")
                else:
                    print("La pila está vacía, no hay elementos para borrar.")

            elif opcion == "3":
                if len(pila) > 0:
                    print("Elementos en la pila (Fondo - Cima):", pila)
                else:
                    print("La pila está actualmente vacía.")

            elif opcion == "4":
                break

            else:
                print("Opción no válida. Ingrese un número del 1 al 4.")

    elif opcion_principal == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Ingrese un número del 1 al 3.")
        continue

    repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").lower()
    if repetir != "s":
        print("Fin del programa. ¡Hasta luego!")
        break