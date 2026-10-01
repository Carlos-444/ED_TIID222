class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Crear nodos
nodo1 = Nodo("Juan")
nodo2 = Nodo("Pedro")
nodo3 = Nodo("Ana")

# Enlazar los nodos
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Recorrer la lista
actual = nodo1

while actual:
    print(actual.dato)
    actual = actual.siguiente