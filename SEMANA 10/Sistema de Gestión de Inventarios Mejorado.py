# supermercado_inventario.py
# Sistema de Inventario para un Supermercado con productos básicos precargados
# Autor: Andrea
# Descripción: Gestión de inventario con menú interactivo, persistencia en archivo y manejo de excepciones.

import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self._verificar_o_crear_archivo()
        self._cargar_desde_archivo()

    def _verificar_o_crear_archivo(self):
        """Verifica si existe el archivo, si no lo crea con productos básicos."""
        if not os.path.exists(self.archivo):
            print("📂 Archivo no encontrado, creando uno nuevo con productos básicos...")
            self.productos = {
                "Arroz": 50,
                "Leche": 30,
                "Pan": 40,
                "Huevos": 60,
                "Manzanas": 25,
                "Azúcar": 20,
                "Aceite": 15
            }
            self._guardar_en_archivo()

    def _cargar_desde_archivo(self):
        """Carga productos desde el archivo al iniciar el programa."""
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    try:
                        nombre, cantidad = linea.strip().split(",")
                        self.productos[nombre] = int(cantidad)
                    except ValueError:
                        print(f"⚠️ Línea inválida en archivo: {linea.strip()}")
        except PermissionError:
            print("⚠️ Error: no tienes permisos para leer el archivo.")

    def _guardar_en_archivo(self):
        """Guarda el inventario actual en el archivo."""
        try:
            with open(self.archivo, "w") as f:
                for nombre, cantidad in self.productos.items():
                    f.write(f"{nombre},{cantidad}\n")
            print("💾 Inventario guardado correctamente en archivo.")
        except PermissionError:
            print("⚠️ Error: no tienes permisos para escribir en el archivo.")

    def agregar_producto(self, nombre, cantidad):
        """Agrega un producto al inventario."""
        self.productos[nombre] = cantidad
        print(f"✅ Producto '{nombre}' añadido con cantidad {cantidad}.")
        self._guardar_en_archivo()

    def actualizar_producto(self, nombre, cantidad):
        """Actualiza la cantidad de un producto existente."""
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            print(f"🔄 Producto '{nombre}' actualizado a cantidad {cantidad}.")
            self._guardar_en_archivo()
        else:
            print(f"⚠️ Error: el producto '{nombre}' no existe en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"🗑️ Producto '{nombre}' eliminado del inventario.")
            self._guardar_en_archivo()
        else:
            print(f"⚠️ Error: el producto '{nombre}' no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos en consola."""
        if self.productos:
            print("\n📦 Inventario del Supermercado:")
            for nombre, cantidad in self.productos.items():
                print(f"- {nombre}: {cantidad} unidades")
        else:
            print("⚠️ El inventario está vacío.")


# Menú interactivo estilo supermercado
def menu():
    inv = Inventario()
    while True:
        print("\n=== 🛒 Menú del Supermercado ===")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                inv.agregar_producto(nombre, cantidad)
            except ValueError:
                print("⚠️ Error: la cantidad debe ser un número entero.")

        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            try:
                cantidad = int(input("Nueva cantidad: "))
                inv.actualizar_producto(nombre, cantidad)
            except ValueError:
                print("⚠️ Error: la cantidad debe ser un número entero.")

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inv.eliminar_producto(nombre)

        elif opcion == "4":
            inv.mostrar_inventario()

        elif opcion == "5":
            print("👋 Saliendo del sistema de inventario...")
            break

        else:
            print("⚠️ Opción inválida, intenta nuevamente.")


if __name__ == "__main__":
    menu()