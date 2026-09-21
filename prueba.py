
# Declaramos un arreglo vacío

arreglo = []

# Pedimos 15 números

for i in range(15):
    dato = int(input("Ingrese un número entre 0 y 500: "))
    arreglo.append(dato)

print("Array original:")
print(arreglo)


for i in range(15):

    # Verificamos si el número no es múltiplo de 5
    if arreglo[i] % 5 != 0:

        # Si no es múltiplo de 5, lo ajustamos al siguiente múltiplo de 5
        arreglo[i] = arreglo[i] + (5 - arreglo[i] % 5)

print("Array cincuerizado:")
print(arreglo)