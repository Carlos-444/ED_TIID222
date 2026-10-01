
from collections import deque   
import time

cola=deque()

cola.append("Ana")
cola.append("Juan")
cola.append("Pedro")

print("Elementos en la cola:")
time.sleep(2)

atendido = cola.popleft()
print(f"Atendiendo a: {atendido}")

#para eliminar es de derecha a izquierda, es decir, el primer elemento que entra es el primero en salir (FIFO)  

time.sleep(2)
print ("siguiente persona en la cola:", cola[0])

