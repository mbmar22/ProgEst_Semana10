# Laboratorio guiado en Python

# Paso 1: Crear nodos y agregar al final
cabeza = None
cola = None

def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}


def agregar_final(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)

    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
    else:
        nuevo["anterior"] = cola
        cola["siguiente"] = nuevo
        cola = nuevo

agregar_final("Inicio")
agregar_final("Catálogo")
agregar_final("Contacto")



# Paso 2: Recorrer hacia adelante y atrás
def mostrar_adelante():
    actual = cabeza

    while actual is not None:
        print(actual["dato"], end = " ↔ " if actual ["siguiente"] else "\n")
        actual = actual["siguiente"]

def mostrar_atras():
    actual = cola

    while actual is not None:
        print(actual["dato"], end = " ↔ " if actual["anterior"] else "\n")
        actual = actual["anterior"]


print("\n2. Recorrer hacia adelante y atrás")
mostrar_adelante()
mostrar_atras()


# Paso 3: Insertar al inicio
def agregar_inicio(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)

    if cabeza is None:
        return nuevo

    else:
        nuevo["siguiente"] = cabeza
        cabeza["anterior"] = nuevo
        cabeza = nuevo

print("\n3. Insertar al inicio")
agregar_inicio("Bienvenida")
mostrar_adelante()
mostrar_atras()


# Paso 4: Eliminar por valor
def eliminar(dato):
    global cabeza, cola 
    actual = cabeza

    while actual is not None and actual["dato"] != dato:
        actual = actual["siguiente"]

    if actual is None:
        return False

    anterior = actual["anterior"]
    siguiente = actual["siguiente"]

    if anterior is None:
        cabeza = siguiente
    else:
        anterior["siguiente"] = siguiente

    if siguiente is None:
        cola = anterior
    else:
        siguiente["anterior"] = anterior
        return True
    
print("\n4. Eliminar por valor")
print("Eliminado:", eliminar("Catálogo"))
mostrar_adelante()
mostrar_atras()



# Retos de Programación
print(("\n---- Retos -----").upper())
print(("\n--- Reto 1 · Buscador bidireccional ---").upper())

def buscar(dato):
    global cabeza
    actual = cabeza

    posicion = 0

    while actual is not None:
        if actual["dato"] == dato:
            return True
        actual = actual["siguiente"]
        posicion += 1
    
    return False

print(buscar("Inicio"))
print(buscar("Catálogo"))



print(("\n--- Reto 2 · Insertar después de un valor ---").upper())

def insertar_despues(referencia, dato):
    actual = cabeza

    while actual is not None:
        if actual["dato"] == referencia:
            nuevo = crear_nodo(dato)

            nuevo["siguiente"] = actual["siguiente"]
            actual["siguiente"] = nuevo

            return True
        
        actual = actual["siguiente"]

    return False


print(insertar_despues("Inicio", "Medio"))
mostrar_atras() # Averiguar por qué no imprime la lista inversa
mostrar_adelante()



print(("\n--- Reto 3 · Historial del navegador ---").upper())

