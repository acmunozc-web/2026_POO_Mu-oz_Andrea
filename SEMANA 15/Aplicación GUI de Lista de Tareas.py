import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas - GUI")
        self.root.geometry("400x450")

        # --- 1. Interfaz Gráfica ---

        # Campo de entrada (Entry)
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)
        # Evento: Presionar Enter para añadir tarea
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.add_button = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task, bg="#4caf50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(btn_frame, text="Marcar Completada", command=self.mark_completed, bg="#2196f3",
                                         fg="white")
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task, bg="#f44336",
                                       fg="white")
        self.delete_button.grid(row=0, column=2, padx=5)

        # Componente de lista (Listbox)
        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Opcional: Doble clic para marcar como completada
        self.tasks_listbox.bind('<Double-Button-1>', lambda event: self.mark_completed())

    # --- 2. Lógica de la Aplicación ---

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpiar entrada
        else:
            messagebox.showwarning("Atención", "Escribe una tarea primero.")

    def mark_completed(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            # Cambiar estado visual: Fondo gris y texto tachado (simulado con color)
            self.tasks_listbox.itemconfig(index, fg="gray", bg="#f0f0f0")
            # Opcional: Agregar prefijo
            current_text = self.tasks_listbox.get(index)
            if "✔ " not in current_text:
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, f"✔ {current_text}")
                self.tasks_listbox.itemconfig(index, fg="gray")
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para marcar.")

    def delete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
