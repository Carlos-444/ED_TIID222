"""
#creaer un arreglo
numeros = [10, 20,30, 40, 50]
print(numeros[2])

#cambiar el valor de una posicion               
numeros [2] = 100
print(numeros)

#para agregar un elemento al final
numeros.append([60, 70])
agregar de otra forma.
numeros.append(60)
numeros.append(70)
print(numeros)


numeros.append([60, 70])
print(numeros[5])

#para imprimir el 60
print(numeros[5][0])

numeros = [10, 20,30, 40]
numeros.insert(2, 25)
print(numeros)

numeros = numeros + [50, 60, 70]
rint(numeros)

numeros = [10, 20, 30]

numeros[len(numeros):] = [40]

print(numeros)


#Ejercicio 1

calificaciones = [70, 85, 90, 65]

calificaciones.append(95)
calificaciones.insert(2, 80)
print(calificaciones)


#ejercicio 2
colores = ["Azul", "Amarillo", "Rosa"]
print(colores)

# Posteriormente, agrega los colores:
colores.extend(["Verde", "Morado", "Rojo"])
print(colores)

#imprimir solo el color morado
print(colores[4])  # Imprime el color en la posición 5 (Morado)
"""


numeros = [10, 20, 30, 40 ]

numeros.extend([50, 67])
print(numeros)

numeros.insert(2, 95)
print(numeros)

print(numeros[2])
print(numeros[6])



print("10", numeros.index(10))
print("20", numeros.index(20))
print("30", numeros.index(30))
print("40", numeros.index(40))
print("50", numeros.index(50))
print("67", numeros.index(67))


