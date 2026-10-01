

#crear un ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#agregamos un nuevo elemento a la matriz
matriz.append([10, 11, 12])

#crear columna en la matriz
for i in range(len(matriz)):
    matriz[i].append(i + 1)  # Agrega un nuevo elemento a cada fila de la matriz    
    print(matriz[i])  # Imprime cada fila de la matriz después de agregar un nuevo elemento




#modificamos un elemento de la matriz
matriz[1][1] = 55  # Cambia el elemento en la segunda

#eliminamos un elemento de la matriz
matriz.pop(0)  # Elimina la primera fila de la matriz

#buscamos un elemento en la matriz
for i in range(len(matriz)):
    print(matriz[i])  # Imprime cada fila de la matriz
    
    
    