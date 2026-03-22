import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry   # external library for DatePicker

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # --- Frame principal para la lista de eventos ---
        frame_lista = ttk.Frame(root)
        frame_lista.pack(padx=10, pady=10, fill="both", expand=True)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill="both", expand=True)

        # --- Frame para entrada de datos ---
        frame_entrada = ttk.Frame(root)
        frame_entrada.pack(padx=10, pady=5, fill="x")

        ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_entrada, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = ttk.Entry(frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
        self.desc_entry = ttk.Entry(frame_entrada, width=30)
        self.desc_entry.grid(row=0, column=5, padx=5, pady=5)

        # --- Frame para botones ---
        frame_botones = ttk.Frame(root)
        frame_botones.pack(padx=10, pady=10)

        ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        ttk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if not hora or not descripcion:
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Selección vacía", "Seleccione un evento para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar el evento?")
        if confirmacion:
            self.tree.delete(seleccionado)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()