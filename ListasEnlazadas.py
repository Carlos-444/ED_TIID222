class Nodo:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None


class ListasEnlazadas:
    def __init__(self):
        self.cabeza = None

    def insertar_nodo_al_inicio(self, numero):
        nuevo_nodo = Nodo(numero)

        # Si la lista está vacía
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        # Si ya tiene nodos, el nuevo apunta al que era la cabeza
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo  

    def insertar_nodo_al_final(self, numero):
        nuevo_nodo = Nodo(numero)

        # Si la lista está vacía
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        # Recorrer hasta el último nodo
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente

        # Conectar el nuevo nodo al final
        actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.numero, "->", end=" ")
            actual = actual.siguiente
        print("None")
        
# Crear la lista
mi_lista = ListasEnlazadas()

# Insertar nodos
mi_lista.insertar_nodo_al_inicio(2)
mi_lista.insertar_nodo_al_inicio(1)
mi_lista.insertar_nodo_al_final(56)

# Imprimir
mi_lista.imprimir_lista()

