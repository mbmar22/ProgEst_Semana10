# Mostrar lista
def mostrar_lista(cabeza):
    actual = cabeza

    while actual is not None:
        print(actual["dato"], end = " -> ")
        actual = actual["siguiente"]

    print("None")


# Crear el nodo
print("4. Crear el nodo")
def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}

ana = crear_nodo("Ana")
mostrar_lista(ana)


# Insertar al inicio
print("\n5. Insertar al inicio")

def insertar_inicio(cabeza, dato):
    nuevo = crear_nodo(dato)
    nuevo["siguiente"] = cabeza
    return nuevo


ana = insertar_inicio(ana, "Luis")
ana = insertar_inicio(ana, "Eva")
mostrar_lista(ana)


# Insertar al final
print("\n6. Insertar al final")

def insertar_final(cabeza, dato):
    nuevo = crear_nodo(dato)

    if not cabeza:
        return nuevo

    actual = cabeza

    while actual["siguiente"] is not None:
        actual = actual["siguiente"]

    actual["siguiente"] = nuevo

    return cabeza

ana = insertar_final(ana, "Denia")
ana = insertar_final(ana, "Clemente")
ana = insertar_inicio(ana, "Valeria")
mostrar_lista(ana)


# Recorrer y mostrar
print("\n7. Recorrer y mostrar")

def mostrar(cabeza):
    actual = cabeza

    while actual is not None:
        print(actual["dato"], end = " -> ")
        actual = actual["siguiente"]

    print("None")

mostrar(ana)


# Buscar un turno
print("\n8. Buscar un turno")

def buscar(cabeza, dato):
    actual = cabeza
    posicion = 0

    while actual is not None:
        if actual["dato"] == dato:
            return posicion
        actual = actual["siguiente"]
        posicion += 1

    return -1

print(buscar(ana, "Ana"))


# Eliminar un turno
print("\n9. Eliminar un turno")

def eliminar(cabeza, dato):
    if cabeza is None:
        return None, False
    
    if cabeza["dato"] == dato:
        return cabeza["siguiente"], True
    
    anterior = cabeza
    actual = cabeza["siguiente"]

    while actual is not None:
        if actual["dato"] == dato:
            anterior["siguiente"] = actual["siguiente"]
            return cabeza, True

        anterior = actual

        actual = actual["siguiente"]

    return cabeza, False

eliminar(ana, "Eva")

mostrar(ana)


# Contar los nodos
print("\n10. Contar los nodos")

def contar(cabeza):
    total = 0
    actual = cabeza
    while actual is not None:
        total += 1
        actual = actual["siguiente"]

    return total


print("Total:", contar(ana))


# -----------------------------------------------------------------------------------------------------

# Prueba integrada
'''
print(("\n--- Prueba Integrada ---").upper())
cabeza = None
cabeza = insertar_final(cabeza, "Ana")
cabeza = insertar_final(cabeza, "Luis")
cabeza = insertar_inicio(cabeza, "Marta")

mostrar(cabeza)

print("Posición de Luis:", buscar(cabeza, "Luis"))
cabeza, eliminado = eliminar(cabeza, "Ana")
print("¿Se eliminó Ana?", eliminado)
mostrar(cabeza)
print("Total:", contar(cabeza))
'''


# -----------------------------------------------------------------------------------------------------

print(("\n---Construir el menú ---").upper())

def menu():
    cabeza = None