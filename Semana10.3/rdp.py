# Retos de Programación
'''
Reto 1 · Buscador bidireccional
Crea buscar(dato), que devuelva True si existe y False si no existe. Compara el recorrido desde cabeza con el recorrido desde cola.
'''

import lista_doble

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

buscar("Hola")


'''
Reto 2 · Insertar después de un valor
Implementa insertar_despues(referencia, dato). Si referencia no existe, devuelve False; si existe, inserta el nuevo nodo y devuelve True.

Pregunta: ¿Cómo cambia cola si insertas después del último nodo?
'''

def insertar_despues(referencia, dato):
    print("Hola")