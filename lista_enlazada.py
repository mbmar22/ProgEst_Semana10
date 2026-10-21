# Crear el nodo
dato = "¡Hola!"

def crear_nodo(dato):
    return {"Dato": dato, "Siguiente": None}

print(crear_nodo(dato))

# Insertar al inicio
def insertar_inicio(cabeza, dato):
    nuevo = crear_nodo(dato)
    nuevo["Siguiente"] = cabeza
    return nuevo

print(insertar_inicio(None, 5))
print(insertar_inicio(5, 8))