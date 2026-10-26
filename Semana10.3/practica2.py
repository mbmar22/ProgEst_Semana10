'''
1. Mostrar lista.
    1.1. Mostrar.
    1.2. Mostrar lista.
    1.3. Mostrar adelante.
    1.4. Mostrar atrás.
2. Crear nodo:
    2.1. Lista enlazada.
    2.2. Lista doble.
3. Insertar al inicio.
    3.1. Lista enlazada.
    3.2. Lista doble.
4. Insertar al final.
    4.1. Lista enlazada.
    4.2. Lista doble.
5. Recorrer.
7. Buscar un turno.
8. Eliminar un turno.
    8.1. Eliminar.
    8.2. Eliminar por valor.
9. Contar los nodos.
10. Atender.
11. Insertar después.
12. Invertir.
13. Buscador bidireccional.
14. Insertar después de un valor.
15. Historial del navegador.
'''

print("\n1. Crear nodo.")
def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}

nombres = crear_nodo("Ana")
print("Se ha creado la lista 'nombres'.")


print("\n2. Mostrar lista.")
def mostrar_lista(cabeza):
    actual = cabeza

    while actual is not None:
        print(actual["dato"], end=" -> ")
        actual = actual["siguiente"]

    print("None")

mostrar_lista(nombres)

def mostrar_atras(cabeza):
    actual = cabeza

    while actual is not None:
        print(actual["dato"], end =" <->" if actual["anterior"] else "\n")
        actual = actual["anterior"]

mostrar_atras(nombres)