 

 #creación de una matriz
matriz = [
    [73, 12, 89, 34],
    [5, 61, 27, 94],
    [46, 18, 80, 35]
]

#agregamos un nuevo elemento a la matriz
matriz.append([39, 22, 69, 17])

print(matriz)
#agregamos una nueva columna a la matriz
print(matriz[1]) 


#buscar elementos de una matriz
for i in matriz:
    if 18 in i:
        print(f"27 encontrado en la fila {i}")
        break
    
    
    #buscar un elemento en la matriz
    for filas in matriz:
        for numeros in filas:
            if numeros == 3:
                print(f"3 encontrado en la fila {filas}")
                break
            
            
            from collections import deque
cola = deque()


