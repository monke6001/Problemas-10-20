import random

def generar_aleatorios():
    print("Número aleatorio uniforme (0-1):", random.random())
    print("Número aleatorio entero (1-100):", random.randint(1, 100))
    print("Número aleatorio con distribución normal (media=0, desviación=1):", random.gauss(0, 1))


generar_aleatorios()
