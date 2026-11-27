class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


def insertar_con_direccion(raiz, valor):
    nuevo = Nodo(valor)
    if raiz is None:
        print(f"-> {valor} agregado como Raíz")
        return nuevo

    actual = raiz
    while True:
        lado = input(
            f"Estás en el nodo {actual.valor}. ¿Hacia dónde va {valor}? (i = izquierda / d = derecha): "
        ).strip().lower()

        if lado == "i":
            if actual.izquierdo is None:
                actual.izquierdo = nuevo
                print(f"-> {valor} agregado a la izquierda de {actual.valor}")
                break
            actual = actual.izquierdo
        elif lado == "d":
            if actual.derecho is None:
                actual.derecho = nuevo
                print(f"-> {valor} agregado a la derecha de {actual.valor}")
                break
            actual = actual.derecho
        else:
            print("Opción no válida. Escribe 'i' o 'd'.")

    return raiz


def imprimir_arbol(nodo, nivel=0, prefijo="Raiz: "):
    if nodo is not None:
        print(" " * nivel + prefijo + str(nodo.valor))
        imprimir_arbol(nodo.izquierdo, nivel + 1, "Izquierdo: ")
        imprimir_arbol(nodo.derecho, nivel + 1, "Derecho: ")


valor_raiz = input("Ingresa el valor de la raíz: ").strip()
raiz = Nodo(valor_raiz)

print("\nÁrbol actual:")
imprimir_arbol(raiz)

while True:
    dato = input("\nIngresa el valor del nuevo nodo (o 'salir' para terminar): ").strip()
    if dato.lower() == "salir":
        break
    if dato == "":
        continue
    raiz = insertar_con_direccion(raiz, dato)
    print("\nÁrbol actual:")
    imprimir_arbol(raiz)

print("\nÁrbol final:")
imprimir_arbol(raiz)
