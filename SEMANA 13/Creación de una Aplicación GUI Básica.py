import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Lista para almacenar datos
datos = []

# Función para agregar información
def agregar():
    texto = entrada.get()
    if texto.strip():
        lista.insert(tk.END, texto)
        datos.append(texto)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para limpiar información
def limpiar():
    lista.delete(0, tk.END)
    datos.clear()

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Botón Agregar
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar)
btn_agregar.pack(pady=5)

# Botón Limpiar
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# Ejecutar aplicación
ventana.mainloop()