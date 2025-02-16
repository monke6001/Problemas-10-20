def convertir_temperatura(valor, escala):
    if escala.lower() == "c":
        return valor * 9/5 + 32  # Celsius a Fahrenheit
    elif escala.lower() == "f":
        return (valor - 32) * 5/9  # Fahrenheit a Celsius
    else:
        return "Escala no válida"


valor = float(input("Ingrese la temperatura: "))
escala = input("Ingrese la escala de conversión (C/F): ")

resultado = convertir_temperatura(valor, escala)
print("Temperatura convertida:", resultado)
