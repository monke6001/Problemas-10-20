def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


lista = [1, 3, 5, 7, 9, 11, 13]
objetivo = int(input("Ingrese el número a buscar: "))

print("Búsqueda Lineal:", busqueda_lineal(lista, objetivo))
print("Búsqueda Binaria:", busqueda_binaria(lista, objetivo))
