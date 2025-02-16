import math

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No tiene soluciones reales"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Una solución: {x}"
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Dos soluciones: {x1}, {x2}"


a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))
print(resolver_ecuacion_cuadratica(a, b, c))
