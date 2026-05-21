
import random

# Número secreto entre 1 y 10
numero_secreto = random.randint(1, 10)
intentos = 0

print(" ¡Adivina el número (entre 1 y 10)!")

while True:
    intento = input("Tu número: ")
    intentos += 1

    if not intento.isdigit():
        print(" Por favor, escribe un número.")
        continue

    intento = int(intento)

    if intento == numero_secreto:
        print(f" ¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("Muy bajo, intenta de nuevo.")
    else:
        print(" Muy alto, intenta otra vez.")