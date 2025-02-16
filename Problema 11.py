def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    return cadena == cadena[::-1]  # Comparar con su inversa


cadena = input("Ingrese una palabra o frase: ")
if es_palindromo(cadena):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
