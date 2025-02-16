# Nombre del archivo
nombre_archivo = "archivo.txt"

# Escribir en el archivo
with open(nombre_archivo, "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.\n")
    archivo.write("Segunda línea del archivo.\n")

# Leer el archivo
with open(nombre_archivo, "r") as archivo:
    print("Contenido del archivo:")
    print(archivo.read())

# Modificar el archivo (agregar una nueva línea)
with open(nombre_archivo, "a") as archivo:
    archivo.write("Nueva línea agregada.\n")

# Leer nuevamente el archivo modificado
with open(nombre_archivo, "r") as archivo:
    print("Contenido actualizado del archivo:")
    print(archivo.read())
