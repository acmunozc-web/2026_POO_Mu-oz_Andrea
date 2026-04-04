import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry.get().strip()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")

def complete_task(event=None):
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(index)
        tasks_listbox.delete(index)
        tasks_listbox.insert(index, f"[✔] {task}")
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para marcarla como completada.")

def delete_task(event=None):
    try:
        index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para eliminarla.")

def close_app(event=None):
    root.destroy()

# Ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Campo de entrada
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<Return>", add_task)  # Atajo Enter

# Botones
btn_add = tk.Button(root, text="Añadir", command=add_task)
btn_add.pack(pady=5)

btn_complete = tk.Button(root, text="Marcar como completada", command=complete_task)
btn_complete.pack(pady=5)

btn_delete = tk.Button(root, text="Eliminar", command=delete_task)
btn_delete.pack(pady=5)

# Lista de tareas
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

# Atajos de teclado
root.bind("<c>", complete_task)   # Tecla C
root.bind("<d>", delete_task)     # Tecla D
root.bind("<Delete>", delete_task) # Tecla Delete
root.bind("<Escape>", close_app)  # Tecla Escape

root.mainloop()
