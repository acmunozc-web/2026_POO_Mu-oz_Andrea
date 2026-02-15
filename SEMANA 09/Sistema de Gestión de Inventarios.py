"""
Sistema de Gestión de Inventarios
---------------------------------
Este programa implementa un sistema simple de inventario para una tienda.
Permite añadir, eliminar, actualizar, buscar y mostrar productos mediante
una interfaz de consola.

Decisiones de diseño:
- Se utilizan clases para aplicar programación orientada a objetos (POO).
- La clase Producto encapsula los atributos básicos de un producto.
- La clase Inventario gestiona una lista de productos y las operaciones sobre ella.
- Se usa un menú interactivo en consola para que el usuario seleccione opciones.
- Para mayor facilidad, al eliminar o actualizar se muestran los productos y
  el usuario selecciona por número en la lista (más intuitivo que escribir el ID).
- Se precargan algunos productos de ejemplo para que el usuario pueda probar
  el sistema sin necesidad de añadirlos manualmente.
"""

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id_producto: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en inventario.
        :param precio: Precio unitario del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """Representación en texto del producto."""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        """Inicializa el inventario como una lista vacía de productos."""
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        Se asegura de que el ID sea único.
        """
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID ya existe.")
        else:
            self.productos.append(producto)
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario según su ID.
        Si no existe, simplemente no lo elimina.
        """
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado (si existía).")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o precio de un producto según su ID.
        """
        for p in self.productos:
            if p.id_producto == id_producto:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos cuyo nombre contenga la cadena ingresada.
        Permite coincidencias parciales.
        """
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def mostrar_todos(self):
        """
        Muestra todos los productos del inventario.
        Si está vacío, informa al usuario.
        """
        if not self.productos:
            print("Inventario vacío.")
        else:
            for i, p in enumerate(self.productos, start=1):
                print(f"{i}. {p}")


def seleccionar_producto(inventario):
    """
    Muestra los productos disponibles y permite seleccionar uno por número.
    Retorna el producto seleccionado o None si la selección es inválida.
    """
    if not inventario.productos:
        print("No hay productos en el inventario.")
        return None
    inventario.mostrar_todos()
    try:
        opcion = int(input("Seleccione el número del producto: "))
        if 1 <= opcion <= len(inventario.productos):
            return inventario.productos[opcion - 1]
        else:
            print("Selección inválida.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None


def menu():
    """
    Menú principal del sistema de inventario.
    Permite al usuario realizar todas las operaciones disponibles.
    """
    inventario = Inventario()

    # Productos precargados para facilitar pruebas
    inventario.añadir_producto(Producto("P001", "Arroz", 50, 1.20))
    inventario.añadir_producto(Producto("P002", "Leche", 30, 0.90))
    inventario.añadir_producto(Producto("P003", "Pan", 100, 0.15))
    inventario.añadir_producto(Producto("P004", "Huevos", 200, 0.10))

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_p, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            producto = seleccionar_producto(inventario)
            if producto:
                inventario.eliminar_producto(producto.id_producto)

        elif opcion == "3":
            producto = seleccionar_producto(inventario)
            if producto:
                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")
                inventario.actualizar_producto(
                    producto.id_producto,
                    cantidad=int(cantidad) if cantidad else None,
                    precio=float(precio) if precio else None
                )

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()