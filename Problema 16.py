def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    num_vocales = sum(1 for c in cadena if c in vocales)
    num_consonantes = sum(1 for c in cadena if c.isalpha() and c not in vocales)
    return num_vocales, num_consonantes


cadena = input("Ingrese una cadena: ")
vocales, consonantes = contar_vocales_consonantes(cadena)
print(f"Número de vocales: {vocales}")
print(f"Número de consonantes: {consonantes}")
