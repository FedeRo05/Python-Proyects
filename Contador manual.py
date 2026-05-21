import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Contador kk")

# Variable del contador
contador = tk.IntVar(value=0)

# Funciones para aumentar y disminuir
def aumentar():
    contador.set(contador.get() + 1)

def disminuir():
    contador.set(contador.get() - 1)

# Etiqueta para mostrar el contador
etiqueta = tk.Label(ventana, textvariable=contador, font=("Helvetica", 32))
etiqueta.pack(pady=20)

# Botón para aumentar
boton_mas = tk.Button(ventana, text="➕ Aumentar", command=aumentar, width=15, height=2)
boton_mas.pack(pady=5)

# Botón para disminuir
boton_menos = tk.Button(ventana, text="➖ Disminuir", command=disminuir, width=15, height=2)
boton_menos.pack(pady=5)

# Ejecutar la interfaz
ventana.mainloop()