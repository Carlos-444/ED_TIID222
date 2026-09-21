""" 
numeros = [10, 20, 30, 40, 50]

print(numeros[2])  # Imprime el tercer elemento del arreglo

numeros[3] = 35  # Cambia el cuarto elemento del arreglo
print(numeros[2])  # Imprime el arreglo modificado
print(numeros)  # Imprime el arreglo completo

numeros.append(60)  # Agrega un nuevo elemento al final del arreglo
print(numeros)  # Imprime el arreglo completo después de agregar un elemento

#obtenemos el tamaño del arreglo
numeros.remove(35)  # Elimina el elemento con valor 35 del arreglo
print(numeros)  # Imprime el arreglo completo después de eliminar un elemento

#eliminar un elemento por su índice
numeros.pop(4)  # Elimina el último elemento del arreglo
print(numeros)  # Imprime el arreglo completo después de eliminar el último elemento



#Arreglos de frutas
fruta = ["manzana", "fresa", "sandia", "Mango", "Melon", "Platano"]
fruta.pop(4)  # Elimina el cuarto elemento del arreglo
print(fruta)  # Imprime el arreglo completo después de eliminar el cuarto elemento

fruta.remove("manzana")  # Elimina el elemento "manzana" del arreglo
print(fruta)  # Imprime el arreglo completo después de eliminar "manzana"

#declaracion de arreglo
arreglo = []
print(fruta)

#declaracion de arreglo con tamaño definido
n = int(input("Ingrese la cantidad de números que desea agregar al arreglo: "))
print(n)

for i in range(n):
    dato = int(input("Ingrese un número: "))
    arreglo.append(dato)  # Agrega el número ingresado al arreglo
    print(arreglo)  # Imprime el arreglo completo después de agregar cada número

#declaracion de un arreglo de 15 elementos
n = int(input("Ingrese la cantidad de números que desea agregar al arreglo "))
print(n)

for i in range(n):
    dato = int(input("Ingrese un número: "))
    arreglo.append(dato)  # Agrega el número ingresado al arreglo
    print(arreglo)  # Imprime el arreglo completo después de agregar cada número
    
"""

    
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