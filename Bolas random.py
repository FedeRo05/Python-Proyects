
import turtle
import random

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("black") # Fondo
pantalla.title("Bolas de colores")

# Lista de colores
colores = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta", "brown", "pink"]

# Crear bolas
for i in range(100):          #for i in range(10)= definir el numero de bolas
    bola = turtle.Turtle()
    bola.color(random.choice(colores)) # Elige un color aleatorio de la lista
    bola.penup()
    bola.shape("circle")
    bola.speed(5)                       # Velocidad de la bola (0 es la más rápida)
                                        #bola.color(colores[i])  color bola cuando se quiere tomar numero de colores especificos

    # Posición aleatoria dentro de un rango visible
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    bola.goto(x, y)

turtle.done()