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
        
        
    def eliminar_nodo_al_inicio(self):

    # Verificar si la lista está vacía
        if self.cabeza is None:
            print("La lista está vacía")
            return

    # Mover la cabeza al siguiente nodo
        self.cabeza = self.cabeza.siguiente
        
        
        
        
    def eliminar_nodo_al_final(self):

    # Verificar si la lista está vacía
        if self.cabeza is None:
            print("La lista está vacía")
            return

    # Verificar si solamente existe un nodo
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

    # Recorrer la lista
        actual = self.cabeza

    # Llegar hasta el penúltimo nodo
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente

    # Desconectar el último nodo
        actual.siguiente = None


# Crear la lista
mi_lista = ListasEnlazadas()

# Insertar nodos
mi_lista.insertar_nodo_al_inicio(2)
mi_lista.insertar_nodo_al_inicio(1)
mi_lista.insertar_nodo_al_final(56)

print("Lista original:")
mi_lista.imprimir_lista()

print("Eliminar al inicio:")
mi_lista.eliminar_nodo_al_inicio()
mi_lista.imprimir_lista()

print("Eliminar al final:")
mi_lista.eliminar_nodo_al_final()
mi_lista.imprimir_lista()