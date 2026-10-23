'''14. Retos de aplicación
1. Atender el primer turno: crea atender(cabeza) que devuelva la nueva cabeza y el nombre atendido; si está vacía, devuelve (None, None). Agrega la opción 6 al menú. Con Ana y Luis debe atender Ana y dejar Luis.
2. Insertar después: crea una función que inserte un nombre después de la primera coincidencia de otro nombre. Si el referente no existe, no modifica la lista e informa el resultado. Ana → Luis, al insertar Eva después de Ana, debe quedar Ana → Eva → Luis.
3. Invertir los enlaces: invierte la lista sin convertirla a una lista de Python ni crear otros nodos. Ana → Luis → Eva debe quedar Eva → Luis → Ana. Comprueba también lista vacía y nodo único.
Para cada reto entrega el código, dos pruebas y un dibujo de las referencias. Las soluciones de los retos deben ser desarrolladas por el estudiante.'''


hola = []
# Reto 1
def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}


def atender(cabeza):
    if cabeza is None:
        return None, None

    nombre = cabeza["dato"]
    nueva_cabeza = cabeza["siguiente"]

    return nueva_cabeza, nombre


# Prueba 1
ana = crear_nodo("Ana")
luis = crear_nodo("Luis")

ana["siguiente"] = luis

cabeza, atendido = atender(ana)

print(atendido)
print(cabeza["dato"])


# Prueba 2
cabeza, atendido = atender(None)

print(cabeza)
print(atendido)


# Reto 2

def insertar_despues(cabeza, referente, nuevo_nombre):
    actual = cabeza

    while actual is not None:
        if actual["dato"] == referente:
            nuevo = crear_nodo(nuevo_nombre)

            nuevo["siguiente"] = actual["siguiente"]

            actual["siguiente"] = nuevo

            return True

        actual = actual["siguiente"]

    return False

# Prueba 1

ana = crear_nodo("Ana")
luis = crear_nodo("Luis")

ana["siguiente"] = luis

insertar_despues(ana, "Ana", "Eva")

# Prueba 2

resultado = insertar_despues(ana, "Pedro", "Eva")

print(resultado)


# Reto 3

def invertir(cabeza):

    anterior = None
    actual = cabeza

    while actual is not None:

        siguiente = actual["siguiente"]

        actual["siguiente"] = anterior

        anterior = actual

        actual = siguiente

    return anterior


# Prueba 1

def mostrar_lista(cabeza):
    actual = cabeza

    while actual is not None:
        print(actual["dato"], end=" -> ")
        actual = actual["siguiente"]

    print("None")

print("Reto 3: Prueba 1")
ana = crear_nodo("Ana")
luis = crear_nodo("Luis")
eva = crear_nodo("Eva")

ana["siguiente"] = luis
luis["siguiente"] = eva

mostrar_lista(ana)

cabeza = invertir(ana)

mostrar_lista(cabeza)


# Prueba 2

cabeza = invertir(None)

mostrar_lista(cabeza)


# Prueba 3

ana = crear_nodo("Ana")

cabeza = invertir(ana)

print(cabeza["dato"])
mostrar_lista(cabeza)